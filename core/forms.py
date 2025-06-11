from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Peca

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuário (RE)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha'}))

class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'codigo', 'preco', 'imagem']