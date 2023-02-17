from django.contrib import admin
from .models import Articale_list



class Articale_listAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','created_date','body']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Articale_list,Articale_listAdmin)
