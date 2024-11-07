from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Laboratorio
from .forms import LaboratorioForm

def lab_list(request):
    labs = Laboratorio.objects.all()
    return render(request, 'labs/lab_list.html', {'labs': labs})

def lab_detail(request, pk):
    lab = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'labs/lab_detail.html', {'lab': lab})

def lab_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labs:lab_list')
    else:
        form = LaboratorioForm()
    return render(request, 'labs/lab_form.html', {'form': form})

def lab_update(request, pk):
    lab = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=lab)
        if form.is_valid():
            form.save()
            return redirect('labs:lab_list')
    else:
        form = LaboratorioForm(instance=lab)
    return render(request, 'labs/lab_form.html', {'form': form})

def lab_delete(request, pk):
    lab = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        lab.delete()
        return redirect('labs:lab_list')
    return render(request, 'labs/lab_confirm_delete.html', {'lab': lab})