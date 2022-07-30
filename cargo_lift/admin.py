from django.contrib import admin
from .models import CargoLift

# Register your models here.
class CargoLiftAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

admin.site.register(CargoLift, CargoLiftAdmin)