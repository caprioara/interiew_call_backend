from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):

    username = forms.CharField(
        label='Enter Username',
        min_length=4,
        max_length=30,
        help_text='Required'
    )

    email = forms.EmailField(
        max_length=100,
        help_text='Required',
        error_messages={
        'required': 'Sorry, we need your email!'
        }
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update(
    #         {}
    #     )
    #     self.fields['email'].widget.attrs.update(
    #         {}
    #     )
    #     self.fields['password'].widget.attrs.update(
    #         {}
    #     )
    #     self.fields['password2'].widget.attrs.update(
    #         {}
    #     )