from django.urls import path
from . import views
urlpatterns=[
    path('',views.sports),
    path('sports/<int:int>',views.details)
    
]