from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'Home'),
    path('products/wire-rope-hoists/', include('wire_rope_hoist.urls'), name = 'Wire Rope Hoists'),
    path('products/chain-hoists/', include('chain_hoist.urls'), name = 'Chain Hoists'),
    path('products/cargo-lifts/', include('cargo_lift.urls'), name = 'Cargo Lifts'),
    path('products/hoist-cranes/', include('hoist_crane.urls'), name = 'Hoist Cranes'),
    path('products/parts-and-accessories/', include('parts_and_accesories.urls'), name = 'Part and Accessories'),
]