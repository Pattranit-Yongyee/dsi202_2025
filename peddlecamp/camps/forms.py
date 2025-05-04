from django import forms
from .models import Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['title', 'description', 'category','participants', 'mode', 'location', 'fee', 'image', 'application_deadline', 
                  'camp_start_date', 'camp_end_date', 'organizer', 'contact_info']
        
        widgets = {
    'application_deadline': forms.DateInput(attrs={'type': 'date'}),
    'camp_start_date': forms.DateInput(attrs={'type': 'date'}),
    'camp_end_date': forms.DateInput(attrs={'type': 'date'}),
}