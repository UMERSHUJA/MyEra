from django.shortcuts import render, redirect, get_object_or_404
from .models import Startup
from django.contrib import messages



def startup(request):
    if request.method == "POST":

        product_name = request.POST['product_name']
        description = request.POST['description']
        image = request.POST['image']
        user_id = request.POST['user_id']
        price = request.POST['price']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        sponsered = 'sponsered' in request.POST
        # sponsered = request.POST['sponsered']
        # if request.POST['sponsered']:
        #     sponsered = True
        # else:
        #     sponsered = False
        
        startup = Startup(product_name=product_name, description=description, image=image, prices=price, facebook=facebook, twitter=twitter, is_sponsered=sponsered, user_id=user_id)
        
        startup.save()

        messages.success(request, 'Your requested has been submitted, wait for the admin response')
        
        return redirect('dashboard')


def editstartup(request, startuplist_id):
    startups = Startup.objects.all().filter(id=startuplist_id)
            
    context= {
        'startups' : startups,
    }
    return render(request, 'pages/editstartup.html', context)


def changeoccur(request, startuplist_id):
    if request.method == 'POST':
        startup = Startup.objects.get(pk = startuplist_id)
        startup.product_name = request.POST['product_name']
        startup.description = request.POST['description']
        startup.image = request.POST['image']
        startup.prices = request.POST['price']
        startup.facebook = request.POST['facebook']
        startup.twitter = request.POST['twitter']
        startup.is_sponsered = 'sponsered' in request.POST
        startup.save()
        messages.success(request, 'You startup has been altered sucessfully!')
        
        return redirect('dashboard')



def delstartup(request, startuplist_id):
    jobs = get_object_or_404(Startup, pk=startuplist_id)
    jobs.delete()
    messages.success(request, 'Your startup has been deleted successfully')
    return redirect('dashboard')
