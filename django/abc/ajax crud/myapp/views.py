from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
#data mokalva mate jasonresponse
#msg moklva mate httprespons

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email =  request.POST.get("email")
        phone = request.POST.get("phone")

        student.objects.create(name=name,email=email,phone=phone)

        return HttpResponse("registration successfilly")
    

def display(request):
    students = student.objects.all()
    return JsonResponse({"students":list(students.values())})