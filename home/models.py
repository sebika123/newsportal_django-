
from django.db import models
#from accounts.models import User


# Create your models here.
class content(models.Model):
    
    
    #author=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    time=models.TimeField()
    image=models.ImageField(upload_to='home')
    def __str__(self):
    
       return self.name
    
    class Meta:
    
        verbose_name='home' 
    
class Details(models.Model):
    id=models.IntegerField(primary_key=True)
    

    author = models.CharField(max_length=255)
    
    name=models.ForeignKey(content, on_delete=models.CASCADE,related_name='names')
    time=models.TimeField()
    
    image=models.ForeignKey(content, on_delete=models.CASCADE,related_name='images')
    content=models.TextField() 
    def __str__(self):
    
       return self.name
    
    class Meta:
    
        verbose_name='details'    