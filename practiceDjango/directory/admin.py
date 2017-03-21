from django.contrib import admin

# Register your models here.
from .models import Item 

class itemAdmin(admin.ModelAdmin):
	list_display = ['title','amount'] 

admin.site.register(Item, itemAdmin)
