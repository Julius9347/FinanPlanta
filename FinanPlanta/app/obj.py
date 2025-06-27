"""
Aqui se agregaran los distintos objetos como plantas a la base de datos
""" 

from models import Planta
import services
import db
# planta inicio menta
# nombrar a las plantas
# secciones ej: semilla(0-100 mil), brote(100-215), retoño(215-345),   
# categorias ej: Jardin, Selva, Tropical, Desierto, Acuaticas  
# tipo ej: cactus
# Lista de plantas predefinidas
plantas = [
    #      Sintaxis para declarar a una nueva planta
    # Planta(
    #     nombre="Cactus",
    #     descripcion="Planta resistente que requiere poco riego.",
    #     categoria="Planta de inicio",
    #     puntos_salud=1,
    #     nivel_crecimiento=1,
    #     motivacion_mensaje="¡Eres tan resistente como un cactus!"
    # ),
]
def registrar_plantas():
    con = db.conectar()
    cur = con.cursor()
    for planta in plantas:
        condiciones = " AND ".join([f"{k} = ?" for k in planta.__dict__.keys()])
        valores = list(planta.__dict__.values())
        query = f"SELECT 1 FROM planta WHERE {condiciones} LIMIT 1"
        cur.execute(query, valores)
        print(f"Verificando planta: {planta.nombre}")
        if not cur.fetchone():
            columna = ", ".join(planta.__dict__.keys())
            placeholders = ", ".join(["?"] * len(planta.__dict__))
            insert_query = f"INSERT INTO planta ({columna}) VALUES ({placeholders})"
            cur.execute(insert_query, valores)
    con.commit()
    cur.close()
    con.close()
    
def menu_registro_plantas():
    while True:
        print("""Bienvenido al registro de plantas.
Opciones disponibles:
1. Inicializar plantas predefinidas en la base de datos.
2. Consultar plantas registradas.
3. Modificar planta.
4. Eliminar planta.
5. Salir.
""")

        opcion = input("Tu opcion: ")
        match opcion:
            case "1":
                registrar_plantas()
            case "2":
                db.verificar_tabla("planta")
            case "3":
                print("en 'Nombre de la tabla' se debe poner 'planta'")
                db.actualizar_valor_desde_consola()
            case "4":
                print("en 'Nombre de la tabla' se debe poner 'planta'")
                db.eliminar_valor_desde_consola()
            case "5":
                print("Saliendo del registro de plantas.")
                break
            case _:
                print("Opción no válida. Por favor, intenta nuevamente.")
            
if __name__ == "__main__":
    menu_registro_plantas()
    # Puedes llamar a menu_registro_plantas() aquí para iniciar el registro de plantas
    # o integrar esta funcionalidad en tu aplicación principal.