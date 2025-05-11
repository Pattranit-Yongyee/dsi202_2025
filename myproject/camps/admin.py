from django.contrib import admin
from .models import Camp, StudentProfile

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


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'education_level', 'hobbies', 'interests')
    search_fields = ('user__email', 'education_level', 'hobbies', 'interests')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'

admin.site.register(StudentProfile, StudentProfileAdmin)
