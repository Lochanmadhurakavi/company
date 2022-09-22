from random import choices
from django.forms import ModelForm
from django import forms
from . models import Apply

class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = ('title', 'first_name', 'last_name',)
        labels = {
            'title': 'Title', 
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            # 'birth_date': 'Date Of Birth', 
            # 'martial_status': 'Martial Status', 
            # 'email': 'Email Address', 
            # 'phone_no': 'Phone Number', 
            # 'address_1': 'Address Line 1', 
            # 'address_2': 'Address Line 2', 
            # 'city': 'City', 
            # 'state': 'State', 
            # 'zipcode': 'Zipcode', 
            # 'years_present': 'Years Present',

        }
        title_choices = [('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')]
        status = [('Single', 'Single'), ('Married', 'Married'), ('Other', 'Other')]
        
        widgets = {
            'title': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Title'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), 
            # 'birth_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Birth Date'}), 
            # 'martial_status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Martial Status'}), 
            # 'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), 
            # 'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}), 
            # 'address_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address No 1'}), 
            # 'address_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address No 2'}), 
            # 'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), 
            # 'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), 
            # 'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), 
            # 'years_present': forms.RadioSelect(attrs={'class': 'form-radio',}),

        }
