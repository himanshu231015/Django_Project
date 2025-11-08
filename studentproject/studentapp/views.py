from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dis(request):
    return HttpResponse("Welcome to Student Management System")
def home(request):
    return HttpResponse("This is the Home Page")