from django.contrib import admin
from .models import WireRopeHoist, WireRopeHoistBrand

# Register your models here.
class WireRopeHoistAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]
    list_filter = ["brand"]
    search_fields = ["name"]

admin.site.register(WireRopeHoist, WireRopeHoistAdmin)
admin.site.register(WireRopeHoistBrand)