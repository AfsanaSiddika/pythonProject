
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ShopForm
from .models import Shop

# Create your views here.
from django.shortcuts import render, redirect


def add_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop-list')  # Redirect to shop list page after adding shop
    else:
        form = ShopForm()
    return render(request, 'shops/add_shop.html', {'form': form})


def shop_list(request):
    # Retrieve all shops from the database
    shops = Shop.objects.all()
    # Render the template with the list of shops
    return render(request, 'shops/shop_list.html', {'shops': shops})


def remove_shop(request, shop_id):
    # Retrieve the shop object or return a 404 error if not found
    shop = get_object_or_404(Shop, pk=shop_id)

    if request.method == 'POST':
        # If the request is a POST request (i.e., form submission), delete the shop
        shop.delete()
        return redirect('shop-list')  # Redirect to shop list page after removing shop

    # If the request is a GET request (i.e., displaying the confirmation page), render the template
    return render(request, 'shops/remove_shop.html', {'shop': shop})


def update_shop(request, shop_id):
    # Retrieve the shop object or return a 404 error if not found
    shop = get_object_or_404(Shop, pk=shop_id)

    if request.method == 'POST':
        # If the request is a POST request (i.e., form submission), update the shop with the new data
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop-list')  # Redirect to shop list page after updating shop
    else:
        # If the request is a GET request (i.e., displaying the form), prepopulate the form with the shop's current data
        form = ShopForm(instance=shop)

    # Render the template with the form
    return render(request, 'shops/update_shop.html', {'form': form, 'shop': shop})
