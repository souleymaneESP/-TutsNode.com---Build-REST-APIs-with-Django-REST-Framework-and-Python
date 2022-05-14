

from django.urls import path,include
from watchmate_app.views import *
urlpatterns = [
    path('list/',movie_list,name="movie-list"),
    path('<int:pk>',movie_detail,name="movie-detail")
]