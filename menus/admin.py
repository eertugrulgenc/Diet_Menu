from pyexpat import model
from django.contrib import admin
from .models import foodInfo
# Register your models here.
class foodInfoAdmin(admin.ModelAdmin):
    list_display = ['id','foodName','foodCalorie']
    class Meta : 
        model = foodInfo

admin.site.register(foodInfo,foodInfoAdmin)