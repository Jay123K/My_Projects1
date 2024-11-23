from django.shortcuts import render,redirect
from .models import Student
from .form import StudentForm
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView,UpdateView
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
# Create your views here.

def Login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect("/")
    
        user=authenticate(username=username,password=password)
        if user is None:
            return redirect("Login")
        else:
            login(request,user)
            return redirect("/")
        
    return render(request,'app1/Login_page.html')


def Register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'User name already exists')
            return redirect("Register")


        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('Login')
    return render(request,'app1/Register_page.html')


def Home(request):
    return render(request,'app1/home.html')


def StudentData(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,"app1/student_page.html",{'form':form})