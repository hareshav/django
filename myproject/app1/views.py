from django.shortcuts import render,redirect
from rest_framework import generics
from .serializer import data
import uuid
# from django.contrib.auth.models import AbstractUser
from .models import UserModels,LocalService,RemoteService,demo
from .services import globaldisplay,localdisplay
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('fname')
        uname+=' '+request.POST.get('lname')
        pword=request.POST.get('password')
        email=request.POST.get('email')
        location='hello'
        user1=UserModels.objects.create_user(uname,email,pword)
        user1.location=location
        user1.save()
        login(request,user1)
        return redirect('home')
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
def searchlocal(request):
    local_list=[]
    for i in LocalService.objects.all():
        d={}
        d['id']=i.id
        d['Name']=i.name
        d['X cood']=i.x_cood
        d['Y cood']=i.y_cood
        d['email']=i.email
        d['services']=i.services
        d['from']=i.from_time
        d['to']=i.to_time
        local_list.append(d)
    if request.method=='POST':
        button=request.POST.get('button')
        type=request.POST.get('stype')
        if button=='search':
            service=request.POST.get('service')
            x_cood=request.POST.get('x_cood')
            y_cood=request.POST.get('y_cood')
        if button!='y':
            if request.user.email=='h@g.com':
                return redirect('signin')
            print((button))
            datetime=request.POST.get('from')
            duration=request.POST.get('duration')
            print(datetime,duration)
            
            local_service_instance = LocalService.objects.get(id=button)
            request.user.onservicelocal=local_service_instance
            request.user.save()
            return HttpResponse("service added")    
    return render(request,'localApply.html',{'local':localdisplay,'localService':local_list})
def searchglobal(request):
    global_list=[]
    for i in RemoteService.objects.all():
        d={}
        d['id']=i.id
        d['Name']=i.name
        d['email']=i.email
        d['services']=i.services
        d['from']=i.from_time
        d['to']=i.to_time
        global_list.append(d)
    if request.method=='POST':
        button=request.POST.get('button')
        type=request.POST.get('stype')
        if button=='search':
            service=request.POST.get('service')
            x_cood=request.POST.get('x_cood')
            y_cood=request.POST.get('y_cood')
        if button!='y':
            if request.user.email=='h@g.com':
                return redirect('signin')
            print((button))
            datetime=request.POST.get('from')
            duration=request.POST.get('duration')
            print(datetime,duration)
            remote_service_instance = RemoteService.objects.get(id=button)
            request.user.onserviceglobal=remote_service_instance
            request.user.save()
            return HttpResponse("service added")    
    return render(request,'remotesearch.html',{'global':globaldisplay,'globalService':global_list})
def apply(request):
    if request.user.email=='h@g.com':
        return redirect('signin')
    if request.method=='POST':
        type=request.POST.get('stype')
        name=request.POST.get('name')
        service=request.POST.get('service')
        fromtime=request.POST.get('fromtime')
        totime=request.POST.get('totime')
        if type=='local':
            x_cood=request.POST.get('x_cood')
            y_cood=request.POST.get('y_cood')
            local=LocalService()
            local.email=request.user.email
            local.password=request.user.password
            local.name=name
            local.services=service
            local.x_cood=x_cood
            local.y_cood=y_cood
            local.from_time=fromtime
            local.to_time=totime
            local.save()
        else:
            remote=RemoteService()
            remote.email=request.user.email
            remote.password=request.user.password
            remote.name=name
            remote.services=service
            remote.from_time=fromtime
            remote.to_time=totime
            remote.save()
    return render(request,'application.html',{'global':globaldisplay,'local':localdisplay})
def logoutuser(request):
    logout(request)
    return redirect('index')
class api(generics.ListCreateAPIView):
    queryset=RemoteService.objects.all()
    serializer_class=data
