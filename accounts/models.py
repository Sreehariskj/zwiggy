from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid

class UserManager(BaseUserManager):
    def create_user(self,email,phone,name,password=None):
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            name = name
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self, email,password=None):
        user = self.create_user(
            email=email,
            password=password,
            #firstname = firstname,
            #lastname = lastname,
            #phone = phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
            
class User(AbstractBaseUser):
    id = models.CharField(max_length =200,unique=True,default=uuid.uuid4,primary_key=True)
    email = models.EmailField(null=False,max_length=100,unique=True)
    phone = models.IntegerField(null=False,unique=True)
    name = models.CharField(null=False,max_length=100)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)


    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['phone','name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email+", "+self.name
    
    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True