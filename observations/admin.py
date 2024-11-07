# observations/admin.py

from django.contrib import admin
from .models import Observacao

class ObservacaoAdmin(admin.ModelAdmin):
    # Exibe apenas os campos 'laboratorio' e 'texto' no admin
    fields = ['laboratorio', 'texto']

    # Filtra o queryset para que professores vejam apenas suas observações
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Professor').exists():
            return qs.filter(usuario=request.user)
        return qs

    # Define o usuário automaticamente ao salvar uma nova observação
    def save_model(self, request, obj, form, change):
        if not change or not obj.usuario:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

# Registrar o modelo com a classe personalizada
admin.site.register(Observacao, ObservacaoAdmin)
