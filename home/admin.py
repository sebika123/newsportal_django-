from django.contrib import admin
from home.models import Content
# Register your models here.

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')


