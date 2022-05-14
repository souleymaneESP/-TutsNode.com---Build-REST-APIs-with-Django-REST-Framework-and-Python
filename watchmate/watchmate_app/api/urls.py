from django.urls import path,include
from watchmate_app.api.views import *
urlpatterns = [
    path('list/',WatchListAV.as_view(),name="movie-list"),
    path('<int:pk>',WatchListDetailAV.as_view(),name="movie-detail"),
    path('stream/',StreamPlatformListAV.as_view(),name="movie-list"),
    # path('<int:pk>',WatchListDetailAV.as_view(),name="movie-detail")
]