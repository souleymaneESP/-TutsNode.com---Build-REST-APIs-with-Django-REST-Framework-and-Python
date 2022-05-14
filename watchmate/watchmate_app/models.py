from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    website=models.URLField(max_length=100)
    


class WatchList(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    platform= models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watch_list")
    avg_rating= models.FloatField(default=0)
    reviews_number=models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title


class Reviews(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    watch_list=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.rating)

