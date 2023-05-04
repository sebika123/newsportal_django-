from django.urls import path
from . import views
urlpatterns=[
    path('like', views.like, name='like'),
    path('comment', views.comment, name='comment')

    
    
]