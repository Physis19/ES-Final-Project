from django import forms
from .models import Observacao

class ObservacaoForm(forms.ModelForm):
    class Meta:
        model = Observacao
        fields = ['laboratorio', 'texto']