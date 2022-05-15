from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include
from user_app.api.views import *

urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', registration, name="registration"),
     path('logout/', logout, name="logout"),
    
]
