from django import forms
from django.contrib.auth.models import User

from myapp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'


class sign_up(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
