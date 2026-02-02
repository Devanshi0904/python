from django.urls import path
from company.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("depts",DeptApi.as_view()),
    path("depts/<id>",DeptUpdateApi.as_view()),
    path("emps/dept/<id>",addEmp,name='addemp'),
    path("emps",getemps,name="emps"),
    path("emps/<id>",EmpById.as_view()),
    path("emps/dept/<id>/<eid>",updateEmp,name='updateEmp')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)