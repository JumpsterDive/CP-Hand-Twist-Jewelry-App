from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfileInfo(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   username = models.CharField(max_length=25,null=True)
   email = models.EmailField()
   firstName = models.CharField(max_length=100)
   lastName = models.CharField(max_length=100)
    
   def __str__(self):
      return self.username 

