from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        help_text='Required',
        label='Username',
        error_messages={
            'required': 'Please enter your username'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'autocomplete':'off'
            }))
    email = forms.EmailField(
        max_length=50,
        label='Email',
        widget=forms.TextInput(attrs={
            'placeholder':'Email',
            'autocomplete':'off'
            }))
    firstName = forms.CharField(
        max_length=50,
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'autocomplete':'off'}))
    lastName = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'autocomplete':'off'}))
    password1 = forms.CharField(
        max_length=30,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'autocomplete':'off',
            "input type":"password"}))
    password2 = forms.CharField(
        max_length=30,
        label='Confirm  Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm  Password',
            'autocomplete':'off',
            "input type":"password"}))

    class Meta:
        model = Account
        fields = (
            'username',
            'firstName',
            'lastName',
            'email',
            'password1',
            'password2',
        )


class AccountAuthForm(ModelForm):
    username = forms.CharField(
        max_length=50,
        help_text='Required',
        label='Username',
        error_messages={
            'required': 'Please enter your Username'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'autocomplete':'off',
            }))
    password = forms.CharField(
        max_length=30,
        label='Password',
        error_messages={
            'required': 'Please enter your password'
        },
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'autocomplete':'off',}))

    class Meta:
        model = Account
        fields = ('username', 'password')
        exclude = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login details")

class AccountUpdateForm(ModelForm):
    username = forms.CharField(
        max_length=50,
        help_text='Required',
        label='Username',
        error_messages={
            'required': 'Please enter your username'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'autocomplete':'off'
            }))
    email = forms.EmailField(
        max_length=50,
        label='Email',
        widget=forms.TextInput(attrs={
            'placeholder':'Email',
            'autocomplete':'off'
            }))
    firstName = forms.CharField(
        max_length=50,
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'autocomplete':'off'}))
    lastName = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'autocomplete':'off'}))

    class Meta:
        model = Account
        fields = ('firstName', 'lastName', 'username', 'email')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('email "%s" is already used.' % email)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('username "%s" is already used.' % username)
    
