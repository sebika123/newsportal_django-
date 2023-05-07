from django.urls import path
from . import views
urlpatterns=[
    path('',views.politics),
    path('<int:id>',views.get_detailp,name='detailp')
    
]