
from django.shortcuts import render
from django.http import HttpResponse
from home.models import content,detailho


def home(request):
    home=content.objects.all()
    return render(request,'home.html',{'home':home} )


   
def detailhome(request,id):
    
    detailho_qs =detailho.objects.filter(id=id)
    detailshome=detailho.objects.get(id=id)
    return render(request,'details.html',{'detailshome':detailshome})
