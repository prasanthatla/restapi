from django import forms
from .models import employee


class employee_form(forms.ModelForm):
    def clean_esal(self):
        input_Sal = self.cleaned_data['esal']
        if input_Sal < 5000:
            raise forms.ValidationError('minimum salary should be 5000')
        return input_Sal

    class Meta:
        model = employee
        fields = '__all__'
