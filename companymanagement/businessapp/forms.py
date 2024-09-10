from django import forms

from businessapp.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_email','contact_phone', 'logo']

