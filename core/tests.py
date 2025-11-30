from django.test import TestCase
from django.urls import reverse
from django.core import mail # Módulo para verificar emails
from core.forms import ContactCourseForm

class ContactCourseTests(TestCase):
    """Testa a funcionalidade do formulário de contato."""

    # Configurações iniciais para os testes
    def setUp(self):
        self.url = reverse('contact')

    def test_contact_page_status_code(self):
        """A página de contato deve estar acessível."""
        # CORREÇÃO 1: Usa self.client
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_contact_form_success(self):
        """Deve enviar o e-mail e mostrar sucesso ao submeter dados válidos."""
        # Reset e verifica a caixa de emails
        self.assertEqual(len(mail.outbox), 0)

        valid_data = {
            'name': 'Aluno Teste',
            'email': 'aluno@teste.com',
            'message': 'Gostaria de saber mais sobre o curso.'
        }

        response = self.client.post(self.url, valid_data, follow=True)

        # CORREÇÃO 2: A contagem de e-mails deve ser 1
        self.assertEqual(len(mail.outbox), 1)

        # Verifica se a mensagem de sucesso está no conteúdo da página renderizada
        self.assertContains(response, 'Sua mensagem foi enviada com sucesso!')

# Teste de Sanidade
class SetupTest(TestCase):
    """Teste de sanidade para garantir que o Pytest/Django está configurado."""

    def test_two_plus_two_equals_four(self):
        """Teste matemático básico que sempre passa."""
        assert 2 + 2 == 4
