from ninja import Router
from productos.models import Producto
from productos.schemas import ProductoSchema, ProductoCreateSchema, ProductoUpdateSchema
from usuarios.auth import AuthBearer
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate
from ninja import File, UploadedFile
from typing import List
from core.utils import search_filter
productos_router = Router(tags=["Productos"])

