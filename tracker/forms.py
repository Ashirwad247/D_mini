from django import forms
from .models import Activity
from datetime import date

class ActivityForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Activity
        fields = ['name', 'description', 'date']

    def clean_date(self):
        activity_date = self.cleaned_data['date']
        if activity_date > date.today():
            raise forms.ValidationError("The date cannot be in the future.")
        return activity_date