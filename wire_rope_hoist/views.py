from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import WireRopeHoist, WireRopeHoistBrand
from .serializers import WireRopeHoistSerializer, WireRopeHoistBrandSerializer

@api_view(['GET'])
def wire_rope_hoists_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    products = WireRopeHoist.objects.all()
    result = paginator.paginate_queryset(products, request)
    serializer = WireRopeHoistSerializer(result, many = True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def wire_rope_hoists_brand_view(request):
    if (request.method == 'GET'):
        brands = WireRopeHoistBrand.objects.all()
        serializer = WireRopeHoistBrandSerializer(brands, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
