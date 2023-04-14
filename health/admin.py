from django.contrib import admin
from health.models import content
# Register your models here.

@admin.register(content)
class contentAdmin(admin.ModelAdmin):
    list_display=('name','time','image')
