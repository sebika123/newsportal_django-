
from django.db import models

# Create your models here.
class content(models.Model):
    name=models.CharField(max_length=255)
    time=models.TimeField()
    image=models.ImageField(upload_to='health')
    def __str__(self):
    
       return self.name
    
    class Meta:
    
        verbose_name=' health' 
    
class Detailh(models.Model):
    id=models.IntegerField(primary_key=True)
    author = models.CharField(max_length=255)
    #author=models.CharField(max_length=255)
    name=models.ForeignKey(content, on_delete=models.CASCADE,related_name='names')
    time=models.TimeField()
    #image=models.ImageField(upload_to='details')
    image=models.ForeignKey(content, on_delete=models.CASCADE,related_name='images')
    content=models.TextField()
    
    
    # def __str__(self):
    
    #    return self.name
    
    # class Meta:
    
    #     verbose_name='detailh' 
    
        
    


    
#detailh = detailh.objects.get(id=1)