from xml.dom import ValidationErr
from watchmate_app.api.serializers import StreamPlatformSerializer
from watchmate_app.models import *
from watchmate_app.api.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework import status,mixins,generics,viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class ReviewsCreate(generics.CreateAPIView):
    serializer_class=ReviewsSerializer
    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self,serializer):
        pk=self.kwargs['pk'] 
        watchlist=WatchList.objects.get(pk=pk)
        review_user=self.request.user
        review_queryset=Reviews.objects.filter(watchlist=watchlist,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You already posted a review")
        serializer.save(watchlist=watchlist,review_user=review_user)



class ReviewsList(generics.ListCreateAPIView):
    serializer_class=ReviewsSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Reviews.objects.filter(watch_list=pk)
    

class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewsSerializer


# class ReviewsDetail(mixins.RetrieveModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class=ReviewsSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)






# class ReviewsList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class=ReviewsSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer



# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True,context={'request':request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         stream_platform = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(stream_platform,context={'request': request})
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer= StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



class StreamPlatformListAV(APIView):
    def get(self,request):
        streamPlatforms = StreamPlatform.objects.all()
        serializer= StreamPlatformSerializer(streamPlatforms,many=True,context={'request': request})
        return Response(serializer.data)
        
    def post(self,request):
        serializer= StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):

    def get(self,request,pk):
        try:
            streamPlatform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'Error':'StreamPlatform not found'},status=status.HTTP_404_NOT_FOUND)
        serializer= StreamPlatformSerializer(streamPlatform,context={'request': request})
        return Response(serializer.data)


    def put(self,request,pk):
        streamPlatform = StreamPlatform.objects.get(pk=pk)
        serializer= StreamPlatformSerializer(streamPlatform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        streamPlatform = StreamPlatform.objects.get(pk=pk)
        streamPlatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class WatchListAV(APIView):
    def get(self,request):
        watchLists = WatchList.objects.all()
        serializer= WatchListSerializer(watchLists,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer= WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetailAV(APIView):

    def get(self,request,pk):
        try:
            watchList = WatchList.objects.get(pk=pk)
        except:
            return Response({'Error':'watchList not found'},status=status.HTTP_404_NOT_FOUND)
        serializer= WatchListSerializer(watchList)
        return Response(serializer.data)


    def put(self,request,pk):
        watchList = WatchList.objects.get(pk=pk)
        serializer= WatchListSerializer(watchList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        watchList = WatchList.objects.get(pk=pk)
        watchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











# @api_view(['GET','POST'])
# def StreamPlatform_list(request):
#     if request.method=='GET':
#         StreamPlatforms = StreamPlatform.objects.all()
#         serializer= StreamPlatformSerializer(StreamPlatforms,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer= StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

    

# @api_view(['GET','PUT','DELETE'])
# def StreamPlatform_detail(request,pk):
#     if request.method=='GET':
#         try:
#             StreamPlatform = StreamPlatform.objects.get(pk=pk)
#         except:
#             return Response({'Error':'StreamPlatform not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer= StreamPlatformSerializer(StreamPlatform)
#         return Response(serializer.data)

#     if request.method=='PUT':
#         StreamPlatform = StreamPlatform.objects.get(pk=pk)
#         serializer= StreamPlatformSerializer(StreamPlatform,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method=='DELETE':
#         StreamPlatform = StreamPlatform.objects.get(pk=pk)
#         StreamPlatform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

