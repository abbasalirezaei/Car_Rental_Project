from django.contrib import admin

from .models import *
# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=['city','pincode']
    list_filter = ("city", )
    search_fields = ("city", )

    
@admin.register(CarDealer)
class CarDealerAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['question']
    list_display=['car_dealer','mobile','area']
    list_filter = ("car_dealer", )
    search_fields = ("city", )
    fieldsets = (
        (None, {
            "fields": (
                'car_dealer',
                'area',
                'mobile',
                'wallet',
            ),
        }),
    )
@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    list_display=['car_name','dealer', 'area','is_available']
    list_filter = ("car_name", )
    search_fields = ('car_name','dealer' )

