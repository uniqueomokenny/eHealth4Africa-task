from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ("full_name", "username", "email", "password1", "password2", "is_medical_practioner")
        model = get_user_model()
        help_texts = {
            'password1': _('Some useful help text.'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'Full Name'
        self.fields['username'].label = None
        self.fields['email'].label = 'Email Address'
        self.fields['is_medical_practioner'].label = 'Register as a medical practioner'



class UserSignInForm(forms.Form):
    username = forms.CharField(max_length=120, help_text="Use your username or email", label="Email or Username")
    password = forms.CharField(widget=forms.PasswordInput)

