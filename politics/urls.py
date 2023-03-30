from django.urls import path
from . import views
urlpatterns=[
    path('',views.politics, ),
    path('politics/<int:int>',views.details)
    
]