from django import forms
from .models import Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['title', 'description', 'category', 'participants', 'mode', 'location', 'fee', 'image',
                  'application_deadline', 'camp_start_date', 'camp_end_date', 'organizer', 'contact_info']

        input_class = 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500'

        widgets = {
            'title': forms.TextInput(attrs={'class': input_class}),
            'description': forms.Textarea(attrs={'class': input_class + ' h-28'}),
            'category': forms.Select(attrs={'class': input_class}),
            'participants': forms.NumberInput(attrs={'class': input_class}),
            'mode': forms.Select(attrs={'class': input_class}),
            'location': forms.TextInput(attrs={'class': input_class}),
            'fee': forms.NumberInput(attrs={'class': input_class}),
            'image': forms.ClearableFileInput(attrs={'class': input_class}),
            'application_deadline': forms.DateInput(attrs={'type': 'date', 'class': input_class}),
            'camp_start_date': forms.DateInput(attrs={'type': 'date', 'class': input_class}),
            'camp_end_date': forms.DateInput(attrs={'type': 'date', 'class': input_class}),
            'organizer': forms.TextInput(attrs={'class': input_class}),
            'contact_info': forms.TextInput(attrs={'class': input_class}),
        }
