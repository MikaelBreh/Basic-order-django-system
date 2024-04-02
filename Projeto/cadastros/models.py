from django.db import models


# Create your models here.
class Clientes(models.Model):
    nome_fantasia = models.CharField(max_length=50)
    razao_social = models.CharField(max_length=50, blank=False, null=False)
    cnpj = models.IntegerField(blank=False, null=False)
    inscricao_estadual = models.IntegerField()
    cep = models.IntegerField(blank=False, null=False)
    endereco = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nome_fantasia + ' - Nome Real: ' + self.razao_social
