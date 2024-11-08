from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Laboratorio
from django.urls import reverse

class LaboratorioModelTest(TestCase):
    def setUp(self):
        self.laboratorio = Laboratorio.objects.create(name="Lab Teste", location="Bloco A")

    def test_laboratorio_creation(self):
        self.assertEqual(self.laboratorio.name, "Lab Teste")
        self.assertEqual(self.laboratorio.location, "Bloco A")

class LaboratorioViewTest(TestCase):
    def setUp(self):
        # Criar grupo de Administrador e usuário administrador
        self.admin_group = Group.objects.create(name="Administrador")
        self.admin_user = User.objects.create_user(username="admin", password="admin123")
        self.admin_user.groups.add(self.admin_group)
        self.admin_user.save()

        # Criar laboratório para testes
        self.laboratorio = Laboratorio.objects.create(name="Lab Teste", location="Bloco A")

    def test_admin_can_access_lab_list(self):
        self.client.login(username="admin", password="admin123")
        response = self.client.get(reverse('labs:lab_list'))
        self.assertEqual(response.status_code, 200)

    def test_admin_can_create_laboratorio(self):
        self.client.login(username="admin", password="admin123")
        response = self.client.post(reverse('labs:lab_create'), {'name': 'Novo Lab', 'location': 'Bloco B'})
        self.assertEqual(response.status_code, 302)  # Redirecionamento após criação
        self.assertTrue(Laboratorio.objects.filter(name='Novo Lab').exists())
