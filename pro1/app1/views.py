from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView,UpdateView

# Create your views here.

def Login_page(request):
    return render(request,'app1/Login_page.html')


def Register_page(request):
    return render(request,'app1/Register_page.html')