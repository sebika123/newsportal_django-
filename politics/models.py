from django.db import models

# Create your models here.
class content(models.Model):
    name=models.CharField(max_length=255)
    time=models.TimeField()
    image=models.ImageField(upload_to='politics')
    
       
    def __str__(self):
    
        return self.name
    
    class Meta:
    
        verbose_name='politics'
    
    
class detailp(models.Model):
    id=models.AutoField(primary_key=True)
    
    
    name=models.ForeignKey(content, on_delete=models.CASCADE,related_name='names')
    time=models.TimeField()
    
    image=models.ForeignKey(content, on_delete=models.CASCADE,related_name='images')
    author = models.CharField(max_length=255)
    contents=models.TextField()
    
    
  
