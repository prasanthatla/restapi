from django import forms
from .models import employee


class empoyee_form(forms.ModelForm):
    def clean_esal(self):
        input_sal=self.cleaned_data['esal']
        if input_sal<5000:
            raise forms.ValidationError('minimum salary should be 5000')

        return input_sal

    class Meta:
        model = employee
        fields = '__all__'
