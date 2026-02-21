from ninja import NinjaAPI
from productos.api import productos_router
from usuarios.api import usuarios_router

api = NinjaAPI(title="BBTITO API", version="1.0")

api.add_router("/productos", productos_router)
api.add_router("/usuarios", usuarios_router)
