import os
import sys
import django
import getpass

# Configurar Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from usuarios.models import Usuario

def crear_usuario():
    nombre = input('Introduce el nombre de usuario: ')
    contraseña = getpass.getpass('Introduce la contraseña: ')
    usuario = Usuario(nombre=nombre)
    usuario.contraseña_hasheada = contraseña  # Guardar la contraseña directamente
    usuario.save()
    print(f'Usuario {nombre} creado con éxito.')  

if __name__ == '__main__':
    crear_usuario()