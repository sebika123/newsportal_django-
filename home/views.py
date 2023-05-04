
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from home.models import content,Details


def home(request):
    home=content.objects.all()
    return render(request,'home.html',{'home':home})



#def details(request):
#    details=home.objects.filter(id=id)
 #   details=home.objects.get(id=id)
  #  return HttpResponse(details[0].content)
   
def details(request, id):
    details_qs =Details.object.filter(id=id)
    details=Details.object.get(id=id)
    return render(request, 'details.html', {'details':details})