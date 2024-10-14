from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=['%d-%m-%Y', '%Y-%m-%d']
    )

    class Meta:
        model = Activity
        fields = ['name', 'description', 'date']
