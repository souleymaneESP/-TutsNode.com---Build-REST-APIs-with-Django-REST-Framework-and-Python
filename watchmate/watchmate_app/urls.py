

from django.urls import path,include
from watchmate_app.views import movie_list
urlpatterns = [
    path('list/',movie_list,name="movie-list")
]