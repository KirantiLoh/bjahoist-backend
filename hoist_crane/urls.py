from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoist_cranes_view, name = 'Chain Hoists View'),
    path('brands', views.hoist_cranes_brand_view, name = 'Chain Hoists Brands View'),

]
