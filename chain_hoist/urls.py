from django.urls import path
from . import views

urlpatterns = [
    path('', views.chain_hoists_view, name = 'Chain Hoists View'),
    path('brands', views.chain_hoists_brand_view, name = 'Chain Hoists Brands View'),

]
