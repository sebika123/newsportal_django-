from django.urls import path
from . import views
urlpatterns=[
    path('',views.sports),
    path('<int:id>',views.details,name='details')
    
]