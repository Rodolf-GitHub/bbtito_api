from ninja import Schema, ModelSchema
from .models import Usuario


class UsuarioSchema(ModelSchema):
    class Meta:
        model = Usuario
        exclude = ["contraseña_hasheada", "token"]


class LoginSchema(Schema):
    nombre: str
    contraseña: str


class TokenSchema(Schema):
    token: str


class DetailSchema(Schema):
    detail: str

