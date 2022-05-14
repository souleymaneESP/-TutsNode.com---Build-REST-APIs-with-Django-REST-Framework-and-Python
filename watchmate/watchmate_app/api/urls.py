from django.urls import path,include
from watchmate_app.api.views import *
urlpatterns = [
    path('list/',MovieListAV.as_view(),name="movie-list"),
    path('<int:pk>',MovieDetailAV.as_view(),name="movie-detail")
]