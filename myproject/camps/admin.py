from django.contrib import admin
from .models import Camp

@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'mode', 'location', 'fee', 'approved')
    list_filter = ('category', 'approved')
    search_fields = ('title', 'location', 'organizer')
    fields = (
        'title','description','category','participants','fee','location','application_deadline','camp_start_date','camp_end_date',
        'organizer','contact_info','image', 'approved'
    )
    actions = ['approve_camps']
    
    def approve_camps(self, request, queryset):
        queryset.update(approved=True)
    approve_camps.short_description = "Approve selected camps"
