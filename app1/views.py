from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        email=request.POST.get('email')
        user1=User.objects.create_user(uname,email,pword)
        user1.save()
        return HttpResponse("USER CREATED")
    return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        print(uname,pword)
        user=authenticate(request,username=uname,password=pword)
        if user is not None:
            login(request,user)
            return HttpResponse("Login successful welcome"+uname)
        else:
            return HttpResponse("Login failed")
    return render(request,'signin.html')
