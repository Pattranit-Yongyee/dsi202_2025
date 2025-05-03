from django import forms
from .models import Camp, StudentProfile
from .models import Camp, CampCategory
import datetime

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['camp_name', 'detail_camp', 'duration_days', 'duration_year', 'seats', 'time_range', 
                  'start_date', 'organizer_name', 'email', 'phone_num', 'place', 'ig', 'facebook', 
                  'line', 'detail_activity', 'poster', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = CampCategory.objects.all()
        self.fields['category'].empty_label = "เลือกหมวดหมู่"
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date', 'min': datetime.date.today})
        self.fields['duration_year'].widget = forms.NumberInput(attrs={'min': datetime.date.today().year})

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        duration_year = cleaned_data.get('duration_year')
        today = datetime.date.today()
        if start_date and start_date < today:
            raise forms.ValidationError({'start_date': 'วันที่เริ่มต้องเป็นวันที่ในอนาคต'})
        if duration_year and duration_year < today.year:
            raise forms.ValidationError({'duration_year': 'ปีต้องเป็นปีในอนาคต'})
        return cleaned_data

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['username', 'major', 'grade', 'hobby', 'interest']