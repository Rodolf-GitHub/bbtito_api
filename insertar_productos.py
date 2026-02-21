import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


import random
from productos.models import Producto

NOMBRES = [
    "Camiseta", "Pantalón", "Vestido", "Sudadera", "Chaqueta", "Falda", "Short", "Blusa", "Abrigo", "Jeans",
    "Zapatos", "Botas", "Sandalias", "Gorra", "Bufanda", "Guantes", "Calcetines", "Chaleco", "Traje", "Polo"
]

for i in range(1000):
    nombre = random.choice(NOMBRES) + f" {random.randint(1, 1000)}"
    precio = round(random.uniform(5, 200), 2)
    para_mujer = random.choice([True, False])
    en_oferta = random.choice([True, False])
    Producto.objects.create(
        nombre=nombre,
        precio=precio,
        para_mujer=para_mujer,
        en_oferta=en_oferta
    )
print("¡1000 productos insertados!")
