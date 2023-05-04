from django.contrib import admin
from health.models import content,Detailh
# Register your models here.

@admin.register(content)
class contentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')
    
@admin.register(Detailh)
class DetailAdmin(admin.ModelAdmin):
    list_display=('name','time','image','author','content')
