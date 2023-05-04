from django.contrib import admin
from politics.models import content,detail
# Register your models here.

@admin.register(content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')
    
    
@admin.register(detail)
class ContentAdmin(admin.ModelAdmin):
    list_display=('name','time','image','author','content')

