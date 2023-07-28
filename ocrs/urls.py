
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Car Rental'                    # default: "Django Administration"
admin.site.index_title = 'Car Rental Administration'                 # default: "Site administration"
admin.site.site_title = 'Car Rental' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer_portal/',include('customer_portal.urls')),
    path('car_dealer_portal/',include('car_dealer_portal.urls')),
    path('',include('home.urls')),
]
