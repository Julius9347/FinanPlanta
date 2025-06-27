"""
Modulo para definir las clases de los objetos que se usaran:
Movimiento
Resgistrar_usuario
Iniciar_seccion
Planta
Gasto
Ingreso
"""
class Movimiento:
    
    def __init__(self, tipo='ingreso', monto=0, descripcion='', fecha=None):
        if tipo not in ['ingreso', 'gasto']:
            raise ValueError("Tipo debe ser 'ingreso' o 'gasto'")
        self.tipo = tipo  # 'ingreso' o 'gasto'
        self.monto = monto
        self.descripcion = descripcion
        self.fecha = fecha

    def __str__(self):
        return f"{self.tipo.capitalize()}: {self.monto} - {self.descripcion}. Fecha: {self.fecha if self.fecha else 'No especificada'}"
    
class Registrar_usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

class Iniciar_seccion:
    def __init__(self, email, contrasena):
        self.email = email
        self.contrasena = contrasena

class Planta:
    """
    Inicializa obejtos Plantas y su salida
    """
    def __init__(self, nombre, descripcion, categoria, puntos_salud, nivel_crecimiento, motivacion_mensaje):
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.puntos_salud = int(puntos_salud)
        self.nivel_crecimiento = int(nivel_crecimiento)
        self.motivacion_mensaje = motivacion_mensaje
        
    def mostrar_planta(self):
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Categoría: {self.categoria}")
        print(f"Puntos de Salud: {self.puntos_salud*100}")
        print(f"Nivel de Crecimiento: {self.nivel_crecimiento*100}")
        print(f"Mensaje de Motivación: {self.motivacion_mensaje}")
