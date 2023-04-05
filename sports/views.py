from django.shortcuts import render
from django.http import HttpResponse
from sports.models import content


def sports(request):
    sports=content.objects.all()
    return render(request,'sports.html',{'sports':sports})



def details(request):
    details=sports.objects.filter(id=id)
    details=sports.objects.get(id=id)
    return HttpResponse(details[0].content)
   