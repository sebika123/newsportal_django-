from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password

# Create your views here.
def login(request):
    if request.method == "POST":
        
        un=request.POST['un']
        pw=request.POST['pw']
        
        user = auth.authenticate(username=un,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return HttpResponse('wrong credentials')
            return redirect('home')
        
        
        
    return HttpResponse('invalid')
      
def register(request):
    if request.method == "POST":
        
        fn=request.POST['fn']
        ln=request.POST['ln']
        em=request.POST['em']
        mb=request.POST['mb']
        ad=request.POST['ad']
        un=request.POST['un']
        pw=make_password(request.POST['pw'])
        user=User(first_name=fn,last_name=ln,email=em,mobile=mb,address=ad,username=un,password=pw)
        user.save()
        return redirect('/home')
    return HttpResponse('invalid')
      
      
def logout(request):
    auth.logout(request)
    return  redirect('/home/')    