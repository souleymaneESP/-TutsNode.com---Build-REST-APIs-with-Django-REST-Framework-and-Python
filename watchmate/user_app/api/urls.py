from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include
from user_app.api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', registration, name="registration"),
    path('logout/', logout, name="logout"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
