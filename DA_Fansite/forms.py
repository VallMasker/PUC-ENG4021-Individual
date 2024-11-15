from django import forms
from .models import Personagem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'icone_URL', 'descricao', 'raca', 'idade']
        exclude = ['usuario']

class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['nome', 'sobrenome', 'username', 'email',
                  'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username