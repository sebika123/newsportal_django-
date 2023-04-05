from django.contrib import admin
from health.models import Content
# Register your models here.

@admin.register(Content)
class contentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')
