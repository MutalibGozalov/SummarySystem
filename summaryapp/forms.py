from dataclasses import field, fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from summaryapp.models import AssingmentModel, ServiceModel


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class AssignmentForm(forms.ModelForm):
#     queryset = ServiceModel.objects.all()
#     service = forms.ModelMultipleChoiceField(queryset = ServiceModel.objects.all(), widget= forms.CheckboxSelectMultiple)
#     class Meta:
#         model = AssingmentModel
#         fields = ["employee", "service", "tip"]

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = AssingmentModel
        fields = ["employee", "service", "tip"]

class ServiceFrom(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields ='__all__'
    
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'put'}))
