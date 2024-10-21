from django.db import models

# Create your models here.
class Camiseta(models.Model):
    nome = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=4)
