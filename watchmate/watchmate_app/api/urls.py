from django.urls import path,include
from watchmate_app.api.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('stream',StreamPlatformVS, basename='streamplatform')




urlpatterns = [
    path('list/',WatchListAV.as_view(),name="movie-list"),
    path('<int:pk>/',WatchListDetailAV.as_view(),name="movie-detail"),
    path('',include(router.urls)),
    # path('stream/',StreamPlatformListAV.as_view(),name="streamplatform-list"),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name="streamplatform-detail"),
    # path('reviews/',ReviewsList.as_view(),name="reviews-list"),
    # path('reviews/<int:pk>',ReviewsDetail.as_view(),name="reviews-detail"),
    path('<int:pk>/review-create/',ReviewsCreate.as_view(),name="reviews-create"),
    path('<int:pk>/reviews/',ReviewsList.as_view(),name="reviews-list"),
    path('reviews/<int:pk>/',ReviewsDetail.as_view(),name="reviews-detail"),
]

