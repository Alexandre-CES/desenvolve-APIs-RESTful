from django.db import models

# Create your models here.
class user(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False,max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome