# observations/tests.py

from django.test import TestCase
from django.contrib.auth.models import User, Group
from labs.models import Laboratorio
from django.urls import reverse

from observations.models import Observacao

class ObservacaoModelTest(TestCase):
    def setUp(self):
        # Criar laboratório e usuário
        self.laboratorio = Laboratorio.objects.create(name="Lab Teste", location="Bloco A")
        self.usuario = User.objects.create_user(username="professor", password="professor123")

        # Criar observação para teste
        self.observacao = Observacao.objects.create(
            laboratorio=self.laboratorio,
            usuario=self.usuario,
            texto="Computador com problemas"
        )

    def test_observacao_creation(self):
        self.assertEqual(self.observacao.texto, "Computador com problemas")
        self.assertEqual(self.observacao.laboratorio, self.laboratorio)
        self.assertEqual(self.observacao.usuario, self.usuario)

class ObservacaoViewTest(TestCase):
    def setUp(self):
        # Criar grupos e usuários
        self.professor_group = Group.objects.create(name="Professor")
        self.professor_user = User.objects.create_user(username="professor", password="professor123")
        self.professor_user.groups.add(self.professor_group)
        self.professor_user.save()

        self.admin_group = Group.objects.create(name="Administrador")
        self.admin_user = User.objects.create_user(username="admin", password="admin123")
        self.admin_user.groups.add(self.admin_group)
        self.admin_user.save()

        # Criar laboratório e observação para testes
        self.laboratorio = Laboratorio.objects.create(name="Lab Teste", location="Bloco A")
        self.observacao = Observacao.objects.create(
            laboratorio=self.laboratorio,
            usuario=self.professor_user,
            texto="Problema no computador"
        )

    def test_professor_can_create_observacao(self):
        self.client.login(username="professor", password="professor123")
        response = self.client.post(reverse('observations:observation_create'), {
            'laboratorio': self.laboratorio.id,
            'texto': 'Novo problema no computador'
        })
        self.assertEqual(response.status_code, 302)  # Redirecionamento após criação
        self.assertTrue(Observacao.objects.filter(texto="Novo problema no computador").exists())

    def test_professor_cannot_access_other_users_observacoes(self):
        self.client.login(username="professor", password="professor123")
        other_user = User.objects.create_user(username="outro_professor", password="senha123")
        outra_observacao = Observacao.objects.create(
            laboratorio=self.laboratorio,
            usuario=other_user,
            texto="Observação de outro usuário"
        )

        response = self.client.get(reverse('observations:observation_detail', args=[outra_observacao.id]))
        self.assertEqual(response.status_code, 404)  # Deve retornar 404, pois o professor não deve acessar observações de outros
