from django.shortcuts import render
from django.http import HttpResponse
from studentapp.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def dis(request):
    return HttpResponse("Welcome to Student Management System")
def home(request):
    return HttpResponse("This is the Home Page")


def reg1(request):
    if request.method=="POST":
        eid=request.POST("eid")
        ename=request.POST("ename")
        esalr=request.POST("esalr")
        eadd=request.POST("eadd")
        unm=request.POST("unm")
        pw=request.POST("pw")
        user = user.objects.create(unm=unm,pw=pw)
        user.save()
        form=Registration.objects.create(eid=eid,ename=ename,esalr=esalr,eadd=eadd,unm=unm,pw=pw)
        form.save()
        return HttpResponse("Registration Successful")
        
    return render(request,"reg1.html")