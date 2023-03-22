from django.db import models

# Create your models here.
class content(models.Model):
    name=models.CharField(max_length=255)
    time=models.TimeField()
    image=models.ImageField(upload_to='politics')
    
    
    
# def __str__(self):
    
#     return self.name
    
# class Meta:
    
#     verbose_name='1. Content'