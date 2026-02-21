from ninja import Router
from productos.models import Producto
from productos.schemas import ProductoSchema, ProductoCreateSchema, ProductoUpdateSchema
from usuarios.auth import AuthBearer
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate
from ninja import File, UploadedFile
from typing import List
from core.utils.search_filter import search_filter
from core.utils.compress_image import compress_image
from core.utils.delete_image_file import delete_image_file
from ninja.responses import Response


productos_router = Router(tags=["Productos"])

@productos_router.get("/listar_todos", response=List[ProductoSchema])
@paginate
@search_filter(['nombre'])
def list_productos(request, busqueda: str = None):
    """Endpoint para listar todos los productos, con soporte de búsqueda por nombre."""
    productos = Producto.objects.all()
    return productos

@productos_router.get("/listar_ofertas", response=List[ProductoSchema])
@paginate
@search_filter(['nombre'])
def list_productos_ofertas(request, busqueda: str = None):
    """Endpoint para listar todos los productos en oferta, con soporte de búsqueda por nombre."""
    productos = Producto.objects.filter(en_oferta=True)
    return productos

@productos_router.get("/listar_para_mujer", response=List[ProductoSchema])
@paginate
@search_filter(['nombre'])
def list_productos_para_mujer(request, busqueda: str = None):
    """Endpoint para listar todos los productos para mujer, con soporte de búsqueda por nombre."""
    productos = Producto.objects.filter(para_mujer=True)
    return productos

@productos_router.get("/listar_para_hombre", response=List[ProductoSchema])
@paginate
@search_filter(['nombre'])
def list_productos_para_hombre(request, busqueda: str = None):
    """Endpoint para listar todos los productos para hombre, con soporte de búsqueda por nombre."""
    productos = Producto.objects.filter(para_mujer=False)
    return productos

@productos_router.post("/crear", response=ProductoSchema, auth=AuthBearer())
def create_producto(request, data: ProductoCreateSchema, imagen: File[UploadedFile] = None):
    """Endpoint para crear un nuevo producto. Requiere autenticación."""
    try:
        producto = Producto.objects.create(**data.dict())
        if imagen:
            compressed_image = compress_image(imagen)
            producto.imagen.save(imagen.name, compressed_image, save=True)
        return producto
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=400)

@productos_router.patch("/actualizar/{producto_id}", response=ProductoSchema, auth=AuthBearer())
def update_producto(request, producto_id: int, data: ProductoUpdateSchema, imagen: File[UploadedFile] = None):
    """Endpoint para actualizar un producto existente. Requiere autenticación."""
    try:
        producto = get_object_or_404(Producto, id=producto_id)
        for attr, value in data.dict(exclude_unset=True).items():
            setattr(producto, attr, value)
        if imagen:
            # Eliminar la imagen anterior si existe
            delete_image_file(producto.imagen)
            compressed_image = compress_image(imagen)
            producto.imagen.save(imagen.name, compressed_image, save=True)
        else:
            producto.save()
        return producto
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=400)

@productos_router.delete("/eliminar/{producto_id}", auth=AuthBearer())
def delete_producto(request, producto_id: int):
    """Endpoint para eliminar un producto existente. Requiere autenticación."""
    try:
        producto = get_object_or_404(Producto, id=producto_id)
        # Eliminar la imagen asociada si existe
        delete_image_file(producto.imagen)
        producto.delete()
        return {"success": True}
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=400)


