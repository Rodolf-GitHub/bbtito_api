from ninja import Schema, ModelSchema
from productos.models import Producto
from typing import Optional

class ProductoSchema(ModelSchema):
    class Meta:
        model = Producto
        fields = "__all__"

class ProductoCreateSchema(Schema):
    nombre: str
    precio: float
    para_mujer: bool = True
    en_oferta: bool = False

class ProductoUpdateSchema(Schema):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    para_mujer: Optional[bool] = None
    en_oferta: Optional[bool] = None