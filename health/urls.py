from django.urls import path
from . import views
urlpatterns=[
    path('',views.health),
    path('politics/<int:int>',views.details)
    
]