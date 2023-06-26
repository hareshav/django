from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model
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
        umail=request.POST.get('usermail')
        pword=request.POST.get('password')
        # username=User.objects.get(email=umail).username
        #error raised when wrong password is provided
        # usermodel=get_user_model()
        try:
            username=User.objects.get(email=umail.lower()).username
            user1=authenticate(request,username=username,password=pword)
            if user1 is not None:
                login(request,user1)
                return HttpResponse("login  not failed")
            else:
                return HttpResponse("password incorrect")
        except Exception as e:
            # return HttpResponse("login failed")
            print(e)
    return render(request,'signin.html')
