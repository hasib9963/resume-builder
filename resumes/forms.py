from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'full_name', 'email', 'phone', 'summary', 'skills', 'experience', 'education']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 5}),
            'education': forms.Textarea(attrs={'rows': 3}),
        }