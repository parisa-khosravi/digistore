from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Store(models.Model):
    name = models.CharField(max_length=100,unique=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse ('store_detail',kwargs={'pk':self.pk})

    
class Product(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='product/',blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    





