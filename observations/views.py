# observations/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Observacao
from .forms import ObservacaoForm
from django.contrib.auth.decorators import login_required

@login_required
def observation_list(request):
    observacoes = Observacao.objects.filter(usuario=request.user)
    return render(request, 'observations/observation_list.html', {'observacoes': observacoes})

@login_required
def observation_detail(request, pk):
    observacao = get_object_or_404(Observacao, pk=pk, usuario=request.user)
    return render(request, 'observations/observation_detail.html', {'observacao': observacao})

@login_required
def observation_create(request):
    if request.method == 'POST':
        form = ObservacaoForm(request.POST)
        if form.is_valid():
            observacao = form.save(commit=False)
            observacao.usuario = request.user
            observacao.save()
            return redirect('observations:observation_list')
    else:
        form = ObservacaoForm()
    return render(request, 'observations/observation_form.html', {'form': form})

@login_required
def observation_update(request, pk):
    observacao = get_object_or_404(Observacao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ObservacaoForm(request.POST, instance=observacao)
        if form.is_valid():
            form.save()
            return redirect('observations:observation_list')
    else:
        form = ObservacaoForm(instance=observacao)
    return render(request, 'observations/observation_form.html', {'form': form})

@login_required
def observation_delete(request, pk):
    observacao = get_object_or_404(Observacao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        observacao.delete()
        return redirect('observations:observation_list')
    return render(request, 'observations/observation_confirm_delete.html', {'observacao': observacao})
