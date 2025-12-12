from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def cart(request):
    return render(request,"cart.html")

def chackout(request):
    return render(request,"chackout.html")

def contact(request):
    return render(request,"contact.html")

def shop(request):
    return render(request,"shop.html")

def login_register(request):
    return render(request,"login_register.html")