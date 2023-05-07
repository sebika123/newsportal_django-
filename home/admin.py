from django.contrib import admin
from home.models import content,Detailho
# Register your models here.

@admin.register(content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')



@admin.register(Detailho)
class DetailAdmin(admin.ModelAdmin):
    list_display=('name','time','image','author','contents')

