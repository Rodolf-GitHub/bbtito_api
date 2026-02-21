from ninja import Router
from usuarios.schemas import UsuarioSchema, LoginSchema, TokenSchema, DetailSchema
from usuarios.models import Usuario
from .auth import GenerateToken

usuarios_router = Router(tags=["Usuarios"])

@usuarios_router.post(
    "/login",
    response={200: TokenSchema, 400: DetailSchema, 404: DetailSchema, 500: DetailSchema},
)
def login_usuario(request, payload: LoginSchema):
    try:
        usuario = Usuario.objects.filter(nombre=payload.nombre).first()
        if not usuario:
            return 404, {"detail": "Usuario no encontrado"}

        if usuario.contraseña_hasheada == payload.contraseña:  # Simplified for example purposes
            usuario.token = GenerateToken.generate()
            usuario.save()
            return 200, {"token": usuario.token}

        return 400, {"detail": "Contraseña incorrecta"}
    except Exception:
        return 500, {"detail": "Error durante el login"}

    