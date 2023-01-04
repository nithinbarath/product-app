from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import random

from .models import Product as ProductModels, User as UserModels
from .serializers.product_serializer import ProductSerializer
from .queue.producer import publish

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = ProductModels.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED )

    def retrieve(self, request, pk=None):
        product = ProductModels.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = ProductModels.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = ProductModels.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = UserModels.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })