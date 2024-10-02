from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMINISTRADOR = 'admin'
    COMUM = 'comum'

    TIPO_USUARIO_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (COMUM, 'Comum'),
    ]

    username = None  # Remover o campo username
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default=COMUM,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email


class Imovel(models.Model):
    numero_contribuinte = models.CharField(max_length=255, unique=True, primary_key=True)
    ano_exercicio = models.IntegerField(null=True)
    codlog_imovel = models.CharField(max_length=255, null=True)
    nome_logradouro = models.CharField(max_length=255, null=True)
    numero_imovel = models.IntegerField(null=True)
    complemento = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255, null=True)
    cep = models.CharField(max_length=20, null=True)
    area_terreno = models.FloatField(null=True)
    area_construida = models.FloatField(null=True)
    area_ocupada = models.FloatField(null=True)
    valor_m2_terreno = models.FloatField(null=True)
    valor_m2_construcao = models.FloatField(null=True)
    ano_construcao_corrigido = models.IntegerField(null=True)
    pavimentos = models.IntegerField(null=True)
    tipo_uso_imovel = models.CharField(max_length=255, null=True)
    fator_obsolescencia = models.FloatField(null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.numero_contribuinte}"
