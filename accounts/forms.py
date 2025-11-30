from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class AccountUserCreationForm(UserCreationForm):
    """
    Formulário de criação de usuário customizado.
    """
    # Adicione campos que queremos no formulário
    email = forms.EmailField(label="E-mail")

    class Meta:
        model = User
        fields = ('username', 'email', 'name')

    def clean_email(self):
        """Garante que o e-mail não seja duplicado no sistema."""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

class AccountUserChangeForm(UserChangeForm):
    """Formulário de edição de usuário customizado (usado no Admin)."""
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'is_active', 'is_staff')

    password = None  # Remove o campo de senha do formulário de edição
