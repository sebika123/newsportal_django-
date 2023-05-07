
from django.shortcuts import render
from django.http import HttpResponse
from home.models import content,Detailho


def home(request):
    home=content.objects.all()
    return render(request,'home.html',{'home':home} )


   
def detail(request,id):
    
    detailho_qs =Detailho.objects.filter(id=id)
    detailho=Detailho.objects.get(id=id)
    return render(request,'details.html',{'detailho':detailho})
