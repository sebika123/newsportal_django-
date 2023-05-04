from django.urls import path
from . import views

urlpatterns=[
    path('',views.health),
    path('<int:id>',views.detailh,name='detailh')
    
]