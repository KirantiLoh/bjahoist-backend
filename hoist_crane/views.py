from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import HoistCrane, HoistCraneBrand
from .serializers import HoistCraneBrandSerializer, HoistCraneSerializer

@api_view(['GET'])
def hoist_cranes_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    products = HoistCrane.objects.all()
    result = paginator.paginate_queryset(products, request)
    serializer = HoistCraneSerializer(result, many = True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def hoist_cranes_brand_view(request):
    if (request.method == 'GET'):
        brands = HoistCraneBrand.objects.all()
        serializer = HoistCraneBrandSerializer(brands, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)