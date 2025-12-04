from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class CustomerProfileManage(BaseUserManager):
    def create_user (self,phone,password=None,**extra_fields):
        if not phone:
            raise ValueError("you must enter your phone")   
        user = self.model(phone=phone,**extra_fields)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_staff",False)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,phone,password=None,**extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone,password,**extra_fields)
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone = models.CharField(max_length=11,unique=True)
    # first_name = models.CharField(max_length=30,blank=True,null=True)
    # last_name = models.CharField(max_length=30,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # balance = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomerProfileManage()
    
    def __str__(self):
        return self.phone





        
        

