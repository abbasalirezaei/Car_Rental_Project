from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','mobile', 'area',]
    list_filter = ("user", )
    search_fields = ('user','area' )


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=['user','car_dealer', 'days','is_complete']
    list_filter = ("user", )
    search_fields = ('user','car_dealer' )

