from django.contrib import admin
from .models import *

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display=['phone','first_name','last_name'] # 'balance' deleted
    ordering=['-create_at']