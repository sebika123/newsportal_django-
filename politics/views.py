from django.shortcuts import render
from django.http import HttpResponse
from politics.models import content


def politics(request):
    politics=content.objects.all()
    return render(request,'politics.html',{'politics':politics})



def details(request):
    detailsp_qs=politics.objects.filter(id=id)
    detailsp=politics.objects.get(id=id)
    return HttpResponse(request,'detailp.html',{'detailsp':detailsp})
   