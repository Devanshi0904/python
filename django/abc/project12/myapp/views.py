from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index (request):
    # if request.GET:
    #     cid = request.GET['cid']
    #     products = Product.objects.filter(category_id= cid)
    # else:
    #     products = Product.objects.all()
    # categories = Category.objects.all()
    return render(request,"index.html")

def getproducts(request):
    catid = request.GET['catid']
    if int(catid) > 0 :
        products = Product.objects.filter(category_id=catid)
        return JsonResponse({"products":list(products.values())})
    else:
        products = Product.objects.all()
        return JsonResponse({"products":list(products.values())})
    
def searchproduct(request):
        q = request.GET['q']
        products = Product.objects.filter(name__startswith=q)
        return JsonResponse({"products":list(products.values())})    

def getcategories(request):
    categories = Category.objects.all()
    return JsonResponse({"categories":list(categories.values())})

@login_required(login_url="login-register")
def accounts (request):
    return render(request,"accounts.html")

@login_required(login_url="login-register")
def cart(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request,"cart.html",{"carts":carts})

def addtocart(request):
    pid = request.GET.get('pid')
    product = Product.objects.get(pk=pid)
    user = request.user
   
   
    if user.is_anonymous:
            return HttpResponse(user)
    else:
        isexist= Cart.objects.filter(user=user,product=product)
        if(len(isexist)>=1):
            isexist[0].qty = isexist[0].qty+1
            isexist[0].save()
            return HttpResponse("product added into cart")
        else:
            Cart.objects.create(product=product,user=user,qty=1)
            return HttpResponse("product added into cart")

@login_required(login_url="login-register")
def checkout (request):
    return render(request,"checkout.html")

def compare (request):
    return render(request,"compare.html")

def details (request):
    pid = request.GET['pid']
    product = Product.objects.get(pk=id)
    return render(request,"details.html",{"product":product})

def login_register (request):
    return render(request,"login-register.html")

def shop (request):
    return render(request,"shop.html")

@login_required(login_url="login-register")
def wishlist (request):
    return render(request,"wishlist.html")

def user_registration (request):
    if request.method =='POST':
        data = request.POST
        uname = data.get('uname')
        email = data.get('email')
        password = data.get('pass')

        u = User(username=uname , email=email)
        u.set_password(password)
        u.save()
        return render(request,'login-register.html',{"msg":"registration successfully !"})
    
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
            return render(request,'login-register.html',{"err":"invalid credentials !"})
        
def user_logout(request):
    logout(request)
    return redirect("index")

