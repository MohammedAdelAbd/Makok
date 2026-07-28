from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from imagekitio import ImageKit
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView

import os
from dotenv import load_dotenv


load_dotenv()  # يقرأ ملف .env


IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")
IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT")
IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")


imagekit = ImageKit(


    private_key=IMAGEKIT_PRIVATE_KEY,


)
URL_ENDPOINT = IMAGEKIT_URL_ENDPOINT

def imagekit_auth(request):
    auth_params = imagekit.helper.get_authentication_parameters()

    return JsonResponse({
        "token": auth_params["token"],
        "expire": auth_params["expire"],
        "signature": auth_params["signature"],
        "publicKey": settings.IMAGEKIT_PUBLIC_KEY
    })

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    def list(self, request):
        orders = Orders.objects.all().order_by('-created_at')
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "تم إنشاء الطلب"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
