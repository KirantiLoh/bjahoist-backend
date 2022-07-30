from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import PartsAndAccessories, PartsAndAccessoriesBrand
from .serializers import PartsAndAccessoriesBrandSerializer, PartsAndAccessoriesSerializer

@api_view(['GET'])
def parts_and_accessories_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    products = PartsAndAccessories.objects.all()
    result = paginator.paginate_queryset(products, request)
    serializer = PartsAndAccessoriesSerializer(result, many = True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def parts_and_accessories_brand_view(request):
    if (request.method == 'GET'):
        brands = PartsAndAccessoriesBrand.objects.all()
        serializer = PartsAndAccessoriesBrandSerializer(brands, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)