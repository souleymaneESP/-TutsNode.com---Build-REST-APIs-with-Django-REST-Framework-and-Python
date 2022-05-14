from watchmate_app.api.serializers import MovieSerializer
from watchmate_app.models import *
from watchmate_app.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer= MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer= MovieSerializer(movie)
    return Response(serializer.data)