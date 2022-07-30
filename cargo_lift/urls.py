from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargo_lifts_view, name = 'Wire Rope Hoists View')
]
