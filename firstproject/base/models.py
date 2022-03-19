from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class title(models.Model):
    name=models.CharField(max_length=250)


class Room(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.ForeignKey(title,on_delete=models.CASCADE)
    message=models.TextField(null=True,blank=True)

    
