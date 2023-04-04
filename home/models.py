
from django.db import models

# Create your models here.
class Contents(models.Model):
    name=models.CharField(max_length=255)
    time=models.TimeField()
    image=models.ImageField(upload_to='home')
    