from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def register(request):
    return render(request, 'profile/register.html')


def login(request):
    return render(request, 'profile/login.html')

def dashboard(request):
    return render(request, 'profile/dashboard.html')
    