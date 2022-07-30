from django.contrib import admin
from .models import ChainHoist, ChainHoistBrand

# Register your models here.
class ChainHoistAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]
    list_filter = ["brand"]
    search_fields = ["name"]

admin.site.register(ChainHoist, ChainHoistAdmin)
admin.site.register(ChainHoistBrand)