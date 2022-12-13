from django.contrib import admin
from .models import user_signup

# Register your models here.

class signupModel(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','mobile','address']

admin.site.register(user_signup,signupModel)