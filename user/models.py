from django.db import models
from health.models import content
from sports.models import content
from politics.models import content
from home.models import content
from accounts.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(content, on_delete=models.CASCADE)
    comment = models.TextField()
    
    

class like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(content, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content')