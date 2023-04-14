from django.shortcuts import render
from django.http import HttpResponse
from health.models import content


def health(request):
    health=content.objects.all()
    return render(request,'health.html',{'health':health})



def details(request):
    details=health.objects.filter(id=id)
    details=health.objects.get(id=id)
    return HttpResponse(details[0].content)
   