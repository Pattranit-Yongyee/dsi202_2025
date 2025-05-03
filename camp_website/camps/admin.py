from django.contrib import admin
from .models import Camp, CampCategory, StudentProfile

@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ['camp_name', 'organizer_name', 'status', 'submit']
    list_filter = ['status', 'category']
    search_fields = ['camp_name', 'organizer_name']
    actions = ['approve_camps', 'reject_camps']

    def approve_camps(self, request, queryset):
        queryset.update(status='approved')
    approve_camps.short_description = "Approve selected camps"

    def reject_camps(self, request, queryset):
        queryset.update(status='rejected')
    reject_camps.short_description = "Reject selected camps"

@admin.register(CampCategory)
class CampCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'user']
