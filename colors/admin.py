from django.contrib import admin
from colors.models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        obj.name = obj.name.upper()
        super().save_model(request, obj, form, change)
