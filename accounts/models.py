from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import Group, Permission


# Create your models here.

class User(AbstractUser):
    mobile=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    groups = models.ManyToManyField(Group, related_name='accounts_users')
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_users')
   



