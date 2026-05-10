from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'Register', RegisterViewSet, basename='register')
router.register(r'Login', LoginViewSet, basename='login')
router.register(r'Users', UserViewSet, basename='users')
 

urlpatterns =  router.urls
     
 

