from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
from .forms import TarefaForm
from .models import Tarefa


def lista_tarefas(request):
    status = request.GET.get("status", "todas")
    tarefas = Tarefa.objects.all()

    if status == "pendentes":
        tarefas = tarefas.filter(concluida=False)
    elif status == "concluidas":
        tarefas = tarefas.filter(concluida=True)
    else:
        status = "todas"

    return render(request, "lista.html", {"tarefas": tarefas, "status": status})


def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tarefas")
    else:
        form = TarefaForm()

    return render(request, "formulario.html", {"form": form, "titulo_pagina": "Nova tarefa"})


def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, "detalhe.html", {"tarefa": tarefa})


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)  # instance = atualiza, não cria
        if form.is_valid():
            form.save()
            return redirect("detalhe_tarefa", pk=tarefa.pk)
    else:
        form = TarefaForm(instance=tarefa)  # formulário já preenchido

    return render(request, "formulario.html", {"form": form, "titulo_pagina": "Editar tarefa"})


@require_POST
def alternar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect("detalhe_tarefa", pk=tarefa.pk)


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == "POST":
        tarefa.delete()
        return redirect("lista_tarefas")

    return render(request, "excluir.html", {"tarefa": tarefa})