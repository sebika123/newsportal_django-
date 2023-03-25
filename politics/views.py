from django.shortcuts import render
from django.http import HttpResponse
from politics.models import content


def politics(request):
    politics=content.objects.all()
    return render(request,'home.html',{'politics':politics})



def details(request):
    details=politics.objects.filter(id=id)
    details=politics.objects.get(id=id)
    return HttpResponse(details[0].content)
   