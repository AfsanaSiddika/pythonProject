# In urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('shops/<int:shop_id>/add-product/', views.add_product, name='add-product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete-product'),
]
