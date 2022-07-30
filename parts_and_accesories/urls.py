from django.urls import path
from . import views

urlpatterns = [
    path('', views.parts_and_accessories_view, name = 'Chain Hoists View'),
    path('brands', views.parts_and_accessories_brand_view, name = 'Chain Hoists Brands View'),

]
