from django import forms
from .models import RetreatOffering

class RetreatOfferingForm(forms.ModelForm):
    class Meta:
        model = RetreatOffering
        fields = ['title', 'description', 'date', 'location', 'image']  # Update fields to match the model
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Ensures date picker is used
        }