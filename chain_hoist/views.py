from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import ChainHoist, ChainHoistBrand
from .serializers import ChainHoistBrandSerializer, ChainHoistSerializer

@api_view(['GET'])
def chain_hoists_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    products = ChainHoist.objects.all()
    result = paginator.paginate_queryset(products, request)
    serializer = ChainHoistSerializer(result, many = True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def chain_hoists_brand_view(request):
    if (request.method == 'GET'):
        brands = ChainHoistBrand.objects.all()
        serializer = ChainHoistBrandSerializer(brands, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)