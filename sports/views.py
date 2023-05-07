from django.shortcuts import render
from django.http import HttpResponse
from sports.models import content,Details


def sports(request):
    sports=content.objects.all()
    return render(request,'sports.html',{'sports':sports})




def details(request,id):
    
    details_qs=Details.objects.filter(id=id)
    details=Details.objects.get(id=id)
    return render(request, 'detailsp.html', {'details':details})
   