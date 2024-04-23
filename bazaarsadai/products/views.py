

from django.shortcuts import render, redirect
from .shop import Shop
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product


def add_product(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.shop = shop
            product.save()
            return redirect('shop-detail', shop_id=shop_id)  # Redirect to shop detail page
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        try:
            product.delete()
            messages.success(request, 'Product deleted successfully.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
        return redirect('shop-detail', shop_id=product.shop.id)  # Redirect to shop detail page after deletion
    return render(request, 'products/delete_product.html', {'product': product})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Product updated successfully.')
                return redirect('shop-detail', shop_id=product.shop.id)  # Redirect to shop detail page after update
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {'form': form})
