from django.shortcuts import render
from myapp.models import student
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
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

def delete_student(request):
    sid = request.GET['sid']
    st = student.objects.get(pk=sid)
    st.delete()
    return HttpResponse ("student deleted")

def getbyid(request):
    sid = request.GET['sid']
    st = student.objects.filter(id=sid)
    return JsonResponse({"student":list(st.values())})

def update_student(request):
     
     if request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get("name")
        email =  request.POST.get("email")
        phone = request.POST.get("phone")

        st = student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.phone=phone
        st.save()

        return HttpResponse("update successfully")
     
def search(request):
    Value = request.GET['value']
    # students = student.objects.filter(name__startswith=Value)
    # students = student.objects.filter(name__startswith=Value) | student.objects.filter(email__startswith=Value) | student.objects.filter(phone__startswith=Value)
    students = student.objects.filter(Q(name__startswith=Value)|Q(email__startswith=Value)|Q(phone__startswith=Value))

    return JsonResponse({"students":list(students.values())})

