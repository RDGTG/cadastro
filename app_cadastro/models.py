    
from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
