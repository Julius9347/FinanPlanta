"""
# La clase services lleva la logica del programa
# Julian Meneses Ocampo 
# 07 de Junio 2025

"""

import db
import hashlib 
from models import Planta
from test.test_long import truediv
# La Función registrar usuario registra un usuario con su nombre, correo y contraseña si se incerta correctamente devuelve True de lo contrario retorna False
def registrar_usuario(usuario):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario(nombre, email, contrasena) VALUES (?, ?, ?)", (usuario.nombre, usuario.email, usuario.contrasena))
    id_usuario = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return True, id_usuario

def registrar_movimiento(mov):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movimiento(id_movimiento, cuenta, categoria, tipo, monto, descripcion, fecha, id_usuario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (mov.id_movimiento, mov.cuenta, mov.categoria, mov.tipo, mov.monto, mov.descripcion, mov.fecha, mov.id_usuario))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def ver_recomendaciones(id_usuario):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recomendacion WHERE id_usuario = ?", (id_usuario,))
    recomendaciones = cursor.fetchall()
    cursor.close()
    conn.close()
    return recomendaciones
    
def establecer_meta_financiera(meta):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO metafinanciera(id_meta, nombre, descripcion, monto, fecha_limite, fecha_creacion, id_usuario) VALUES (?, ?, ?, ?, ?, ?, ?)", (meta.id_meta, meta.nombre, meta.descripcion, meta.monto, meta.fecha_limite, meta.fecha_creacion, meta.id_usuario))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def iniciar_seccion(email, contrasena):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT email, contrasena FROM usuario WHERE email = ?", (email,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        contrasena_guardada = resultado[1]
        hash_input = hashlib.sha256(contrasena.encode()).hexdigest()
        if hash_input == contrasena_guardada:
            print("Se ha iniciado seccion correctamente!")
            return True
        else:
            print("contraseña incorrecta o invalida")
            return False
    else:
        print("No se ha encontrado registro")
        return False
    
def menu_inicial_cuenta_nueva(id_usuario, monto):
    if monto >= 0 and monto <= 100000:
        elegir_planta_para_usuario_inicio(id_usuario)

def registrar_planta(planta):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO IF NOT EXISTS planta(nombre, descripcion, categoria, puntos_salud, nivel_crecimiento, motivacion_mensaje) VALUES (?, ?, ?, ?, ?, ?)", (planta.nombre, planta.descripcion, planta.categoria, planta.puntos_salud, planta.nivel_crecimiento, planta.motivacion_mensaje))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def obtener_plantas_disponibles_categoria_planta_inicio():
    con = db.conectar()
    cur = con.cursor()
    cur.execute("SELECT id_planta, nombre, descripcion, categoria, puntos_salud, nivel_crecimiento, motivacion_mensaje FROM planta WHERE categoria = 'Planta de inicio'")
    plantas = cur.fetchall()
    cur.close()
    con.close()
    return plantas

def obtener_datos_del_usuario(id_usuario):
    con = db.conectar()
    cur = con.cursor()
    cur.execute("SELECT id_usuario, nombre, email FROM usuario WHERE id_usuario = ?", (id_usuario,))
    usuario = cur.fetchone()
    cur.close()
    con.close()
    if usuario:
        return usuario
    else:
        print("No se encontraron datos del usuario.")
        return None
    
def asignar_planta_a_usuario(id_usuario, id_planta):
    con = db.conectar()
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO usuario_planta (id_usuario, id_planta) VALUES (?, ?)", (id_usuario, id_planta))
    con.commit()
    cur.close()
    con.close()

def elegir_planta_para_usuario_inicio(id_usuario):
    while True:
        usuario = obtener_datos_del_usuario(id_usuario)
        plantas = obtener_plantas_disponibles_categoria_planta_inicio()
        print("\n Plantas disponibles:")
        for idx, p in enumerate(plantas, 1):
            print(f"{idx}. {p[1]}: ({p[2]})")
            
        eleccion = int(input("Elige el numero de la planta que deseas: ")) - 1
        
        try: 
            idx = eleccion
            if 0 <= idx < len(plantas):
                datos = plantas[idx]
                planta = Planta(*datos[1:])
                print(f"\nInformacion sobre {planta.nombre}:")
                planta.mostrar_planta()
                confirmar = input("¿Deseas elegir esta planta? (si/no): ").strip().lower()
                if confirmar == 'si':
                    asignar_planta_a_usuario(id_usuario, datos[0])
                    print(f"Planta {planta.nombre} asignada correctamente al usuario {usuario[1]}.")
                    break
                else:
                    print("Planta no asignada. Elige otra planta.")
            else:
                print("Opción no válida. Por favor, elige un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número valido.")
            
#def home_de_aplicacion():
    