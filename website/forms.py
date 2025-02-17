from django import forms
from django.forms import ModelForm
from . models import careermodel


class CareerForm(ModelForm):
    class Meta:
        model=careermodel
        fields =[ 'first_name','Last_name','gender','phone_no','email','age','nationality','current_location','attach_cv',]
