from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class AccountUserCreationForm(UserCreationForm):
    """
    Formulário de criação de usuário customizado.
    Herdamos do UserCreationForm do Django para garantir a segurança da senha.
    """
    # Adicionamos o campo email ao formulário
    email = forms.EmailField(label="E-mail")

    class Meta:
        # Apontamos para o nosso model User
        model = User
        fields = ('username', 'email', 'name')

    def clean_email(self):
        """Garante que o e-mail não seja duplicado no sistema (Validação customizada)."""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

class AccountUserChangeForm(UserChangeForm):
    """Formulário de edição de usuário customizado."""
    class Meta:
        model = User
        # Lista os campos que podem ser editados pelo usuário
        fields = ('username', 'email', 'name')

    # Remove o campo de senha do formulário de edição (apenas por boas práticas)
    password = None
