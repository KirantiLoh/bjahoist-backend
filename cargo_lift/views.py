from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import CargoLift
from .serializers import CargoLiftSerializer

@api_view(['GET'])
def cargo_lifts_view(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    products = CargoLift.objects.all()
    result = paginator.paginate_queryset(products, request)
    serializer = CargoLiftSerializer(result, many = True)
    return paginator.get_paginated_response(serializer.data)