from django.contrib import admin
from .models import Student, Camp

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'major', 'grade', 'save')
    search_fields = ('username', 'email', 'major')
    list_filter = ('major', 'grade', 'save')

@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ('camp_name', 'organize_camp', 'start_date', 'final_date', 'place', 'price', 'submit')
    search_fields = ('camp_name', 'organize_camp', 'place')
    list_filter = ('start_date', 'final_date', 'submit')
