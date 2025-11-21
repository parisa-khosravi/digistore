from django.contrib import admin
from .models import *

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display=['name','owner','description']
    list_filter=['name']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['store','name','price','description','image']
    # ordering=['-crate_at']