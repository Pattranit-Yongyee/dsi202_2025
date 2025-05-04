from django.contrib import admin
from .models import Camp

@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'mode', 'location', 'fee')
    list_filter = ('category', 'mode')
    search_fields = ('title', 'location', 'organizer')
    fields = (
        'title','description','category','participants','fee','mode','location','application_deadline','camp_start_date','camp_end_date',
        'organizer','contact_info','image',
    )