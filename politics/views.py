from django.shortcuts import render
from django.http import HttpResponse
from politics.models import content,detailp


def politics(request):
    politics=content.objects.all()
    return render(request,'politics.html',{'politics':politics})



def get_detailp(request,id):
    detailp_qs=detailp.objects.filter(id=id)
    detailsp=detailp.objects.get(id=id)
    return render(request,'detailp.html',{'detailp':detailsp})
   