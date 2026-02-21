from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    contraseña_hasheada = models.CharField(max_length=64)
    token = models.CharField(max_length=64, blank=True, null=True)
    class Meta:
        db_table = 'usuarios'

