from rest_framework import serializers
from watchmate_app.models import *


class ReviewsSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Reviews
        # fields="__all__"
        exclude=('watch_list',)



class WatchListSerializer(serializers.ModelSerializer):
    reviews= ReviewsSerializer(many=True, read_only=True)
    
    class Meta:
        model=WatchList
        fields="__all__"
        # exclude=['active']

    # def validate(self,data):
    #     if data['title']==data['description']:
    #         raise serializers.ValidationError("Name and Title should not be similar")
    #     return data

    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watch_list= WatchListSerializer(many=True,read_only=True)
    class Meta:
        model=StreamPlatform
        fields="__all__"


# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short")
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description= serializers.CharField()
#     active= serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance

#     def validate(self,data):
#         if data['title']==data['description']:
#             raise serializers.ValidationError("Name and Title should not be similar")
#         return data


    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    