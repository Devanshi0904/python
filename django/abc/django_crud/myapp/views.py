from django.shortcuts import render,redirect
from myapp.models import student

# Create your views here.
def home(request):
    students = student.objects.all()
    return render(request,"home.html",{"students":students})

def register_student(request):
    students = student.objects.all()
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    if not id :
        student.objects.create(name=name , email=email , age=age)
        return render(request, 'home.html' , {'success': 'student registered successfully',"students":students})
    else:
        st = student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.age = age
        st.save()
        return render(request, 'home.html' , {'success': 'student update successfully',"students":students})


# def display (request):
#     students = student.objects.all()
#     return render(request,"display.html",{"students":students})

def delete_student (request):
    id = request.GET.get("id")
    st = student.objects.get(pk=id)
    st.delete()
    students = student.objects.all()
    return redirect("home")

def edit_student (request):
   

    id = request.GET.get("id")
    st = student.objects.get(pk=id)
    students = student.objects.all()
    return render(request,'home.html',{'st':st,"students":students})