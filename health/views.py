from django.shortcuts import render
from django.http import HttpResponse
from health.models import content,Detailh


def health(request):
    health=content.objects.all()
    return render(request,'health.html',{'health':health})



def detailh(request,id):
    
    detailh_qs=Detailh.objects.filter(id=id)
    detailh=Detailh.objects.get(id=id)
    return render(request, 'detailh.html', {'detailh':detailh})
   