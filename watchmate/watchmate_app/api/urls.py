from django.urls import path,include
from watchmate_app.api.views import *
urlpatterns = [
    path('list/',WatchListAV.as_view(),name="movie-list"),
    path('<int:pk>',WatchListDetailAV.as_view(),name="movie-detail"),
    path('stream/',StreamPlatformListAV.as_view(),name="streamplatform-list"),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name="streamplatform-detail"),
    path('reviews/',ReviewsList.as_view(),name="reviews-list"),
    path('reviews/<int:pk>',ReviewsDetail.as_view(),name="reviews-detail"),
]