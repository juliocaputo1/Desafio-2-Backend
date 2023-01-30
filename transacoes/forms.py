from django import forms


class EnviarArquivoForm(forms.Form):
    file = forms.FileField()