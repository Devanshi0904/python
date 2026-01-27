from django.urls import path
from company.views import *

urlpatterns = [
    path("depts",DeptApi.as_view()),
    path("depts/<id>",DeptUpdateApi.as_view()),
    path("emps/dept/<id>",addEmp,name='addemp'),
    path("emps",getemps,name="emps")
]