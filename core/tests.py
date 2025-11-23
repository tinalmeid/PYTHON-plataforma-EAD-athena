from django.test import TestCase

class SetupTest(TestCase):
    """Teste de sanidade para garantir que o Pytest/Django está configurado."""

    def test_one_plus_one_equals_two(self):
        """Teste matemático básico que sempre passa."""
        assert 1 + 1 == 2
