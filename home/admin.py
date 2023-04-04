from django.contrib import admin
from home.models import Contents
# Register your models here.

@admin.register(Contents)
class contentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')


