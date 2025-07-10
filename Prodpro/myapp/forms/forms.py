from django import  forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

#     custom validatiom
def custom_validation(x):
    data=re.findall("[a-zA-Z0-9]+[@][a-zA-Z]+.[a-z]{3}",x)
    print(data)
    if not data:
        raise ValidationError("Enter a valid custom email format.")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password',"is_staff"]

class EmployeeRegistrationForm(forms.Form):


    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),validators=[custom_validation])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    conf_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # form level validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        conf_password = cleaned_data.get("conf_password")

        if password and conf_password and password != conf_password:
            self.add_error("conf_password","password is not matching")
    # field lavel validation
    def clean_last_name(self):
        last_name=self.cleaned_data['last_name']
        if any(c.isdigit() for c in last_name):
            self.add_error('last_name','should not contain any digit')
        else:
            return  last_name




