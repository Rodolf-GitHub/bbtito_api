from django.db import models
from core.models import BaseModel

# Create your models here.
class Producto(BaseModel):
    nombre = models.CharField(max_length=255,  default="ropa")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    para_mujer = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    en_oferta = models.BooleanField(default=False)