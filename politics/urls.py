from django.urls import path
from . import views
urlpatterns=[
    path('',views.politics),
    path('/<int:id>',views.detailp,name='detailp')
    
]