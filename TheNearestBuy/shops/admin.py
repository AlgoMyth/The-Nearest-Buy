from django.conf import settings
from django.contrib import admin
from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude','item_desc','cost')
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude','item_desc','cost')
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )