from django.shortcuts import render, redirect
from .models import Startup
from django.contrib import messages



def startup(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        description = request.POST['description']
        image = request.POST['image']
        price = request.POST['price']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        if request.POST['sponsered']:
            sponsered = True
        else:
            sponsered = False

        startup = Startup(product_name=product_name, description=description, image=image, prices=price, facebook=facebook, twitter=twitter, is_sponsered=sponsered)
        
        startup.save()

        messages.success(request, 'Your requested has been submitted, wait for the admin response')
        
        return redirect('dashboard')


