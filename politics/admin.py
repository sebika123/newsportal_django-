from django.contrib import admin
from politics.models import content,detailp
# Register your models here.

@admin.register(content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')
    
    
@admin.register(detailp)
class DetailAdmin(admin.ModelAdmin):
    list_display=('name','time','image','author','contents')

