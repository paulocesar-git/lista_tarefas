from django.db import models

# Create your models here.

class Tarefa(models.Model):
    PRIORIDADES = [
        ("baixa", "Baixa"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(choices = PRIORIDADES)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titulo