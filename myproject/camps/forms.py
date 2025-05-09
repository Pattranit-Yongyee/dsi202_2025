from django import forms
from .models import Camp
from .models import UserProfile

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



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['grade_level', 'other_grade', 'hobbies', 'interests']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['grade_level'] = forms.ChoiceField(
            choices=[('', 'เลือกระดับชั้น')] + UserProfile._meta.get_field('grade_level').choices,
            widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
        )
        self.fields['other_grade'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'ระบุระดับชั้นอื่นๆ'})
        self.fields['hobbies'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'งานอดิเรก (คั่นด้วยเครื่องหมาย ,)'})
        self.fields['interests'].widget.attrs.update({'class': 'w-full p-2 border rounded', 'placeholder': 'ความสนใจ (คั่นด้วยเครื่องหมาย ,)'})