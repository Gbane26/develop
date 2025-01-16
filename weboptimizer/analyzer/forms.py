from django import forms
from .models import Analysis

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ['uploaded_file']