from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url="login-register")
def cart(request):
    return render(request,"cart.html")

@login_required(login_url="login-register")
def chackout(request):
    return render(request,"chackout.html")

def contact(request):
    return render(request,"contact.html")

def shop(request):
    return render(request,"shop.html")

@login_required(login_url="login-register")
def login_register(request):
    return render(request,"login_register.html")
 

def user_registration(request):
    if request.method == 'POST':
        data = request.POST
        uname = data.get('uname')
        email = data.get('email')
        password = data.get('pass')

        u= User(username=uname , email=email)
        u.set_password(password)
        u.save()
        return render(request,"login_register.html",{"msg":"registeration successfully !!"})

def user_login(request):
    if request.method =='POST':
        data = request.POST
        uname = data.get('uname')
        password = data.get('pass')
        u = authenticate(username=uname , password=password)

        if u is not None:
            login(request,u)
            return redirect("index")
        else:
            return render(request,'login_register.html',{"err":"invalid credentials !"})

def user_logout(request):
    logout(request)
    return redirect("index")