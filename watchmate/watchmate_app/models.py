from django.db import models


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

    def __str__(self):
        return self.title