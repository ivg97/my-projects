from django import forms

class LoginForm(forms.Form):
    '''Forms autorisation'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #
    # PasswordInput -
