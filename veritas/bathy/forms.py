from django import forms
from .models import SubmittedFile

class FileSubmissionForm(forms.ModelForm):
    class Meta:
        model = SubmittedFile
        fields = ['submitted_file']
        widgets = {
            'submitted_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
