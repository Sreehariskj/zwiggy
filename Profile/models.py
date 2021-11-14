from django.db import models
from accounts.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField()
    
    def __str__(self):
        return self.user.name