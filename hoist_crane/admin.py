from django.contrib import admin
from .models import HoistCrane, HoistCraneBrand

# Register your models here.
class HoistCraneAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]
    list_filter = ["brand"]
    search_fields = ["name"]

admin.site.register(HoistCrane, HoistCraneAdmin)
admin.site.register(HoistCraneBrand)