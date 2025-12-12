from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    fruits = fruit.objects.all()
    if request.method=='POST':
        name = request.POST['name']
        price= request.POST["price"]
        colour = request.POST['colour']

        fruit.objects.create(name=name,price=price,colour=colour)
        return render(request,"index.html",{"fruits":fruits})

    else: 
        return render(request,"index.html",{"fruits":fruits})
    
def delete_fruit(request):
    id = request.GET['id']
    fru = fruit.objects.get(pk=id)
    fru.delete()
    return redirect('index')

def edit_fruit(request):
    fruits = fruit.objects.all()
    if request.method=='POST':
        id = request.POST['id']
        name = request.POST['name']
        price= request.POST["price"]
        colour = request.POST['colour']

        fru = fruit.objects.get(pk=id)
        fru.name=name
        fru.price=price
        fru.colour=colour
        fru.save()
        
        return render(request,"index.html",{"fruits":fruits})
    else:
        id = request.GET['id']
        fru = fruit.objects.get(pk=id)
        return render(request,'index.html',{'fru':fru,"fruits":fruits})

