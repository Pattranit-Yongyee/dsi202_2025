from django import forms
from .models import Camp
from .models import StudentProfile

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
            'participants': forms.TextInput(attrs={'class': input_class, 'placeholder': 'เช่น 50 คน'}),
            'mode': forms.Select(attrs={'class': input_class}),
            'location': forms.TextInput(attrs={'class': input_class}),
            'fee': forms.TextInput(attrs={'class': input_class, 'placeholder': 'เช่น 500 บาท'}),
            'image': forms.ClearableFileInput(attrs={'class': input_class}),
            'application_deadline': forms.DateInput(attrs={'type': 'date', 'class': input_class}),
            'camp_start_date': forms.DateInput(attrs={'type': 'date', 'class': input_class}),
            'camp_end_date': forms.DateInput(attrs={'type': 'date', 'class': input_class}),
            'organizer': forms.TextInput(attrs={'class': input_class}),
            'contact_info': forms.TextInput(attrs={'class': input_class}),
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['education_level', 'hobbies', 'interests']
        widgets = {
            'education_level': forms.Select(),
            'hobbies': forms.TextInput(attrs={
                'placeholder': 'เช่น อ่านหนังสือ, เล่นกีฬา, โปรแกรมมิ่ง (คั่นด้วย comma)',
                'class': 'w-full p-3 border border-gray-300 rounded-lg'
            }),
            'interests': forms.TextInput(attrs={
                'placeholder': 'เช่น วิทยาศาสตร์, ศิลปะ, เทคโนโลยี (คั่นด้วย comma)',
                'class': 'w-full p-3 border border-gray-300 rounded-lg'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['education_level'].label = 'ระดับชั้น'
        self.fields['hobbies'].label = 'งานอดิเรก'
        self.fields['interests'].label = 'ความสนใจ'

    def clean_hobbies(self):
        hobbies = self.cleaned_data.get('hobbies')
        if hobbies and ',' not in hobbies:
            raise forms.ValidationError('กรุณาคั่นงานอดิเรกด้วยเครื่องหมาย comma (,)')
        return hobbies

    def clean_interests(self):
        interests = self.cleaned_data.get('interests')
        if interests and ',' not in interests:
            raise forms.ValidationError('กรุณาคั่นความสนใจด้วยเครื่องหมาย comma (,)')
        return interests
