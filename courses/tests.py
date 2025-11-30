from django.test import TestCase
from model_bakery import baker
from .models import Course

class CourseModelTest(TestCase):
    """Testes unitários para o modelo Course."""

    def test_create_course(self):
        """Deve criar um cursos com sucesso."""
        course = baker.make(Course, name="Python Pro", _quantity=1,)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(course[0].name, 'Python Pro')
