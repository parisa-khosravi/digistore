from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display=['phone','is_customer','is_seller']
    list_filter=['is_customer','is_seller','is_active','is_staff']
    fieldsets=(
        ('personal onfo',{'fields':('phone',)}),
        ('roles',{'fields':('is_customer','is_seller')}),
        ('permission',{'fields':('is_active','is_staff')}),
    )