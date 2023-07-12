from django.shortcuts import render,redirect
# from django.contrib.auth.models import AbstractUser
from .models import UserModels,LocalService
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        email=request.POST.get('email')
        location=request.POST.get('location')
        user1=UserModels.objects.create_user(uname,email,pword)
        user1.location=location
        user1.save()
        return HttpResponse("USER CREATED")
    return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        umail=request.POST.get('usermail')
        pword=request.POST.get('password')
        # username=User.objects.get(email=umail).username
        #error raised when wrong password is provided
        # usermodel=get_user_model()
        try:
            username=UserModels.objects.get(email=umail.lower()).username
            user1=authenticate(request,username=username,password=pword)
            if user1 is not None:
                login(request,user1)
                return redirect('home')
            else:
                return HttpResponse("password incorrect")
        except Exception as e:
            # return HttpResponse("login failed")
            print(e)
    return render(request,'signin.html')
def home(request):
    return render(request,'home.html')
def apply(request):

    if request.method=='POST':
        name=request.POST.get('name')
        service=request.POST.get('service')
        location=request.POST.get('location')
        fromtime=request.POST.get('fromtime')
        totime=request.POST.get('totime')
        print(name,fromtime,totime)
        local=LocalService()
        local.email=request.user.email
        local.password=request.user.password
        local.name=name
        local.services=service
        local.location=location
        local.from_time=fromtime
        local.to_time=totime
        local.save()
    return render(request,'application.html')
def logoutuser(request):
    logout(request)
    return redirect('index')
