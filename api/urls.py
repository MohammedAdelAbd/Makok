from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
 

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'images', ProductImageViewSet, basename='images')
router.register('orders', OrderViewSet, basename='orders')


urlpatterns = router.urls
urlpatterns = [
    path("imagekit-auth/", imagekit_auth, name="imagekit_auth"),
    path('', include(router.urls)),
]