from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')

def about (request):
    return render(request,'about.html')

def blog (request):
    return render(request,'blog.html')

def contact (request):
    return render(request,'contact.html')

def service (request):
    return render(request,'service.html')

def team (request):
    return render(request,'team.html')

def login (request):
    return render(request,'login.html')

def register (request):
    return render(request,'register.html')

def profile (request):
    return render(request,'profile.html')

def account_setting(request):
    return render(request,"account_setting.html")