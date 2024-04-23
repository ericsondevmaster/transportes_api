from django.contrib import admin
from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        obj.name = obj.name.upper()
        super().save_model(request, obj, form, change)
