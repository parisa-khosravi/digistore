from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile',verbose_name='کاربر')
    phone = models.CharField(max_length=11,unique=True,verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=30,blank=True,null=True,verbose_name='نام')
    last_name = models.CharField(max_length=30,blank=True,null=True,verbose_name='نام خانوادگی') 
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='اعتبار')
    email=models.EmailField(blank=True,null=True,verbose_name='ایمیل')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='پروفایل'
        verbose_name_plural='پروفایل ها'
        ordering=['-create_at']

    def __str__(self):
        return self.phone

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def profile_manage(sender,instance,created,**kwargs):
    phone=f'{instance.phone}'.strip()
    if created:
        Profile.objects.create(user=instance,phone=phone)
    else:
        Profile.objects.update_or_create(user=instance,defaults={'phnoe':phone})

