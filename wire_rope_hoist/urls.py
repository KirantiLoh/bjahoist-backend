from django.urls import path
from . import views

urlpatterns = [
    path('', views.wire_rope_hoists_view, name = 'Wire Rope Hoists View'),
    path('brands', views.wire_rope_hoists_brand_view, name = 'Wire Rope Hoists Brand View'),
]
