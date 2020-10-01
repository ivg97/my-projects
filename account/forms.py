from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    '''Forms autorisation'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #
    # PasswordInput -

class UserRegistrationForm(forms.ModelForm):
    '''Form for registrations users'''
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        '''validation forms and return error'''
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    '''let users change name, lastname, e-mail'''
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    '''let change user additionally '''
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')