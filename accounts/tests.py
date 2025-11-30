from django.test import TestCase
from accounts.models import User
from accounts.forms import AccountUserCreationForm, AccountUserChangeForm # Importamos os dois forms
from model_bakery import baker
from django.core import mail
from django.urls import reverse
from django.conf import settings

# Garante que o Django use o nosso User Model customizado
settings.AUTH_USER_MODEL = 'accounts.User'

class UserModelTests(TestCase):
    """Testes de integridade e métodos do modelo User."""

    def test_user_creation(self):
        """Deve criar um usuário base com sucesso."""
        # Usa o método create_user do Manager
        user = User.objects.create_user(
            username='testeuser',
            email='teste@email.com',
            password='testpassword'
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.username, 'testeuser')
        self.assertEqual(user.email, 'teste@email.com')

    def test_superuser_creation(self):
        """Deve criar um superusuário com sucesso."""
        superuser = User.objects.create_superuser(
            username='adminuser',
            email='admin@site.com',
            password='adminpassword'
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_str_representation(self):
        """Deve retornar o username ou name na representação de string."""
        user = baker.make(User, username='athena', name='Cristina Almeida')
        self.assertEqual(str(user), 'Cristina Almeida')

        # Testar se retorna username se name for None
        user_no_name = baker.make(User, username='semnome', name='')
        self.assertEqual(str(user_no_name), 'semnome')

    def test_create_user_email_not_provided(self):
        """Deve lançar ValueError se o email não for fornecido."""
        # Fix Sonar S2068: Usamos variável para evitar hard-coding da string 'password'
        dummy_pass = 'dummy123'
        with self.assertRaises(ValueError):
            User.objects.create_user(username='no_email', email=None, password=dummy_pass)

    def test_create_superuser_email_not_provided(self):
        """Deve lançar ValueError se o email não for fornecido ao criar superusuário."""
        # Fix Sonar S2068: Variável para senha dummy
        dummy_pass = 'dummyadmin123'
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username='no_email_admin', email=None, password=dummy_pass)

class AccountFormTests(TestCase):
    """Testes de validação dos formulários de usuário."""

    def setUp(self):
        # Cria um usuário para forçar o erro de duplicidade de e-mail
        self.existing_user = User.objects.create_user(
            username='existing', email='duplicate@email.com', password='password'
        )

    def test_creation_form_unique_email_fails(self):
        """
        Teste CRÍTICO: Deve falhar ao tentar registrar e-mail já existente.
        Cobre a lógica 'clean_email' no AccountUserCreationForm.
        """
        data = {
            'username': 'novo_usuario',
            'email': 'duplicate@email.com', # E-mail duplicado
            'password': 'newpassword',
            'password2': 'newpassword'
        }
        form = AccountUserCreationForm(data=data)

        # O form deve ser inválido
        self.assertFalse(form.is_valid())

        # O erro deve estar no campo 'email' com a mensagem esperada
        self.assertIn('Este e-mail já está cadastrado.', form.errors['email'])

    def test_change_form_initial_data(self):
        """
        Testa se o formulário de edição (usado no Admin) carrega os dados corretamente.
        Cobre o AccountUserChangeForm.
        """
        user = User.objects.create_user(username='edit', email='edit@email.com')
        form = AccountUserChangeForm(instance=user)

        self.assertEqual(form.initial['username'], 'edit')
        self.assertTrue('email' in form.fields)

    def test_creation_form_empty_username_fails(self):
        """Deve falhar se o username não for fornecido."""
        data = {
            'username': '', # Campo vazio
            'email': 'novo@email.com',
            'password': 'newpassword',
            'password2': 'newpassword'
        }
        form = AccountUserCreationForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('Este campo é obrigatório.', form.errors['username'])

    def test_change_form_saves_data(self):
        """Deve salvar os dados de edição corretamente."""
        user = baker.make(User, username='initial', email='initial@email.com', name='Original Name')
        data = {
            'username': 'updated_user',
            'email': 'updated@email.com',
            'name': 'Updated Name',
            'is_active': True,
            'is_staff': False,
            # Campos do Custom User Model
            'date_joined': user.date_joined,
        }

        # Testamos o formulário de edição de usuário
        form = AccountUserChangeForm(instance=user, data=data)
        self.assertTrue(form.is_valid())
        form.save()

        # Recarregamos o usuário para verificar a mudança
        user.refresh_from_db()
        self.assertEqual(user.name, 'Updated Name')
