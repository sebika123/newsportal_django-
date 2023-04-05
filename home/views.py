
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Content


def home(request):
    home=Content.objects.all()
    return render(request,'home.html',{'home':home})



def details(request):
    details=home.objects.filter(id=id)
    details=home.objects.get(id=id)
    return HttpResponse(details[0].content)
   