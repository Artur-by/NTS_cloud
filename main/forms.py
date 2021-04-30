from django import forms

class userForms(forms.Form):
    УНП = forms.CharField(min_length=9,max_length=9)
    Пользователь = forms.CharField()
    Пароль = forms.CharField(min_length=8, max_length=100)