from django import forms


class FormGuessNumber(forms.Form):
    number = forms.IntegerField(label="Введите число", widget=forms.TextInput())