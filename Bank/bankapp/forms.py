from django import forms
from django.db import models

class RegistrationForm(forms.Form):
    name = forms.CharField()
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[(‘male’,‘Male’), (‘female’, ‘Female’), (‘transgender’, ‘Transgender’)])
    phone_number = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ChoiceField(choices=[(‘thrissur’, ‘Thrissur’), (‘ernamkulam’, ‘Ernamkulam’), (‘palakkad’, ‘Palakkad’), (‘kottayam’, ‘Kottayam’), (‘trivandrum’, ‘Trivandrum’)])
    branch = forms.ChoiceField(choices=)
    account_type = forms.ChoiceField(choices=[(‘savings’, ‘Savings’), (‘current’, ‘Current’)])
    materials_required = forms.MultipleChoiceField(choices=[(‘debit’, ‘Debit Card’), (‘credit’, ‘Credit Card’), (‘cheque’, ‘Chequebook’)], widget=forms.CheckboxSelectMultiple)