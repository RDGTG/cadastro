from django import forms
from .models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'empresa', 'email', 'senha']



class LoginForm(forms.Form):
        class Meta:
            nome = forms.CharField(max_length=100, label='Nome de Usuário')
            senha = forms.CharField(widget=forms.PasswordInput, label='Senha')




