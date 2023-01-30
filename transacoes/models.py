from django.db import models

class EnviarArquivo(models.Model):
    cnab_file = models.FileField(upload_to="uploads")

class Transacoes (models.Model):
    type = models.CharField(max_length=1)
    data = models.DateField()
    value= models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)