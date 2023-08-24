class ErrorDeAutenticacion(Exception):
    pass

def requerir_autenticacion_usuario(func):
    def envoltura(usuario, *args, **kwargs):
        if usuario.get('rol') == 'usuario':
            return func(usuario, *args, **kwargs)
        else:
            raise ErrorDeAutenticacion("Se requiere autenticación de usuario")
    return envoltura

def requerir_autenticacion_admin(func):
    def envoltura(usuario, *args, **kwargs):
        if usuario.get('rol') == 'admin':
            return func(usuario, *args, **kwargs)
        else:
            raise ErrorDeAutenticacion("Se requiere autenticación de administrador")
    return envoltura

def requerir_autenticacion_superusuario(func):
    def envoltura(usuario, *args, **kwargs):
        if usuario.get('rol') == 'superusuario':
            return func(usuario, *args, **kwargs)
        else:
            raise ErrorDeAutenticacion("Se requiere autenticación de superusuario")
    return envoltura

base_de_datos_usuarios = {
    'usuario123': {'contraseña': 'claveusuario', 'rol': 'usuario'},
    'admin456': {'contraseña': 'claveadmin', 'rol': 'admin'},
    'superusuario789': {'contraseña': 'clavesuper', 'rol': 'superusuario'}
}

@requerir_autenticacion_usuario
def funcion_usuario(usuario):
    return "Función de usuario accedida"

@requerir_autenticacion_admin
def funcion_admin(usuario):
    return "Función de administrador accedida"

@requerir_autenticacion_superusuario
def funcion_superusuario(usuario):
    return "Función de superusuario accedida"

def autenticar():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if nombre_usuario in base_de_datos_usuarios and base_de_datos_usuarios[nombre_usuario]['contraseña'] == contraseña:
        return base_de_datos_usuarios[nombre_usuario]
    else:
        raise ErrorDeAutenticacion("La autenticación falló")

try:
    usuario_autenticado = autenticar()
    print(funcion_usuario(usuario_autenticado))

    admin_autenticado = autenticar()
    print(funcion_admin(admin_autenticado))

    superusuario_autenticado = autenticar()
    print(funcion_superusuario(superusuario_autenticado))

except ErrorDeAutenticacion as e:
    print(f"Fallo en la autenticación: {e}")
