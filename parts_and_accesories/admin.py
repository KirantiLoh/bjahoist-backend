from django.contrib import admin
from .models import PartsAndAccessories, PartsAndAccessoriesBrand

# Register your models here.
class PartsAndAccessoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]
    list_filter = ["brand"]
    search_fields = ["name"]

admin.site.register(PartsAndAccessories, PartsAndAccessoriesAdmin)
admin.site.register(PartsAndAccessoriesBrand)