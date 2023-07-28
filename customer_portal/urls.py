from django.urls import path,include, re_path
from customer_portal.views import *
# from django.conf.urls import url
app_name='customer'
urlpatterns = [
    path('index/',index,name='index'),
    path('login/',login,name='login'),
    path('auth/',auth_view,name='auth'),
    path('logout/',logout_view,name='logout'),
    path('register/',register,name='register'),
    path('registration/',registration,name='registration'),
    path('search/',search,name='search'),
    path('search_results/',search_results,name='search_results'),
    path('rent/',rent_vehicle,name='rent'),
    path('confirmed/',confirm,name='confirmed'),
    path('manage/',manage,name='manage'),
    path('update/',update_order,name='update'),
    path('delete/',delete_order,name='delete'),
]
