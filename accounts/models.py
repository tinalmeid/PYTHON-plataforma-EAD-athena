from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager # Importamos BaseUserManager
from django.core import validators
import re

# --- 1. GERENCIADOR CUSTOMIZADO ---
class AccountUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        # Fail Fast: Garantir que o email existe
        if not email:
            raise ValueError('O e-mail deve ser fornecido para a criação do usuário.')
        if not username:
            raise ValueError('O nome de usuário deve ser fornecido.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Fail Fast: Garantir que o email existe
        if not email:
            raise ValueError('O e-mail deve ser fornecido para o superusuário.')

        return self.create_user(username, email, password, **extra_fields)

# --- 2. O MODELO DE USUÁRIO ---
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        'O nome de usuário só pode conter letras, dígitos ou os seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    is_superuser = models.BooleanField('Superusuário?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    # Usamos o nosso manager customizado
    objects = AccountUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
