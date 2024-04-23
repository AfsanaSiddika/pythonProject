from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_list, name='shop-list'),  # URL for shop list page
    path('add/', views.add_shop, name='add-shop'),  # URL for adding shop
    path('<int:shop_id>/remove/', views.remove_shop, name='remove-shop'),  # URL for removing shop
    # Define other URL patterns as needed
]
