from django import forms

class YogaLoginForm(forms.Form):
    username = forms.CharField(label="Имя (Логин)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))