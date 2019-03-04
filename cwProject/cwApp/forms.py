from django import forms
from .models import FitnessModel


# model based form
class FitnessForm(forms.ModelForm):
    class Meta:
        model = FitnessModel
        fields = '__all__'
