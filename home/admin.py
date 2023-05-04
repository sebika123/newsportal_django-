from django.contrib import admin
from home.models import content,Details
# Register your models here.

@admin.register(content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')



@admin.register(Details)
class DetailAdmin(admin.ModelAdmin):
    list_display=('name','time','image','author','content')

