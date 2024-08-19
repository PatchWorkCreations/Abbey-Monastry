from django import forms
from .models import RetreatOffering

class RetreatOfferingForm(forms.ModelForm):
    class Meta:
        model = RetreatOffering
        fields = ['title', 'description', 'date', 'end_date', 'location', 'image', 'registration_link']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
