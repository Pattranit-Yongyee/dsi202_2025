from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'description', 'detail', 'image')
    search_fields = ('title', 'type', 'description', 'detail', 'image')