""" 
db.py contiene el motor de base de datos SQLite. Aqui se gestionan los diferentes datos con los que trabajará la aplicacion "FinanPlanta"
 Tablas:    1. usuario
            2. categoria
            3. cuenta
            4. notificacion
            5. planta
            6. transacciones
            7. movimiento
            8. presupuesto
            9. ahorro
            10. inversion
            11. gasto
            12. ingreso
            13. porcentaje_acumulado
            14. estadistica_financera
            15. meta_financiera
            16. logro
            17. recomendaciones
            18. configuracion
cada tabla contiene atributos(columnas), cada atributo tiene un tipo de dato, cada tabla tiene una llave primaria, todas las tablas tiene a id_usuario como llave foranea,
tambien se cuenta con restricciones en los atributos
"""
# importa la base de datos SQLite3 y sus funcionalidades
import sqlite3
from sqlalchemy import inspect, create_engine
# importa la libreria de SQLAlchemy para manejar la base de datos

def conectar_engine():
    # Cambia la URL por la de tu base de datos
    engine = create_engine("sqlite:///D:/Python/python_projects/FinanPlanta/finanzas.db")
    return engine

# se conecta a la base de datos que esta guardado en D:/Python/python_projects/FinanPlanta/finanzas.db
def conectar():
    """Se conecta a la base de datos SQLite de la aplicacion"""
    return sqlite3.connect("D:/Python/python_projects/FinanPlanta/finanzas.db")

# crea las tablas si no existen para la base de datos con sus atributos, tipo de datos, restriccioes, llaves primarias y llaves foraneas
def crear_tablas(): 
    
    tablas_sql = {
        "usuario_planta": """
    CREATE TABLE IF NOT EXISTS usuario_planta (
        id_usuario INTEGER,
        id_planta INTEGER,
        fecha_asignacion DATE DEFAULT (DATE('now')),
        PRIMARY KEY (id_usuario, id_planta),
        FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
        FOREIGN KEY(id_planta) REFERENCES planta(id_planta)
    )
""",
        "usuario": """
                CREATE TABLE IF NOT EXISTS usuario (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL, 
                    email TEXT UNIQUE NOT NULL, 
                    contrasena TEXT NOT NULL, 
                    fecha_registro DATE DEFAULT(DATE('now'))
                )
    """,

    "categoria": """
                CREATE TABLE IF NOT EXISTS categoria (
                    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL, 
                    descripcion TEXT NOT NULL, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "cuenta": """
                CREATE TABLE IF NOT EXISTS cuenta (
                    id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    tipo TEXT, 
                    saldo REAL, 
                    id_usuario INTEGER,
                    porcentaje_asignado REAL,
                    fecha_creacion DATE,
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "notificacion": """
                CREATE TABLE IF NOT EXISTS notificacion (
                    id_notificacion INTEGER PRIMARY KEY AUTOINCREMENT, 
                    mensaje TEXT, 
                    fecha DATE, 
                    leida BOOLEAN, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "planta": """
                CREATE TABLE IF NOT EXISTS planta (
                    id_planta INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL,
                    descripcion TEXT, 
                    fecha_inicio DATE DEFAULT(DATE('now')) NOT NULL,
                    categoria TEXT, 
                    estado_salud TEXT CHECK(estado_salud IN ('Excelente', 'Buena', 'Regular', 'Mala')),
                    puntos_salud INTEGER DEFAULT 0, 
                    estado_financiero TEXT, 
                    nivel_crecimiento INTEGER DEFAULT 1,
                    ultima_actualizacion DATE DEFAULT(DATE('now')),
                    motivacion_mensaje TEXT,
                    progreso_ahorro REAL,
                    num_metas_logradas INTEGER,
                    alerta_estres BOOLEAN,
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "transacciones": """
                CREATE TABLE IF NOT EXISTS transacciones (
                    id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT, 
                    tipo TEXT, 
                    cuenta_origen INTEGER,
                    cuenta_destino INTEGER,
                    monto REAL, 
                    descripcion TEXT, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "movimiento": """
                CREATE TABLE IF NOT EXISTS movimiento (
                    id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT, 
                    tipo TEXT, 
                    cuenta INTEGER,
                    categoria INTEGER,
                    monto REAL, 
                    descripcion TEXT, 
                    fecha DATE, 
                    id_usuario INTEGER,
                    FOREIGN KEY(cuenta) REFERENCES cuenta(id_cuenta), 
                    FOREIGN KEY(categoria) REFERENCES categoria(id_categoria),
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "presupuesto": """
                CREATE TABLE IF NOT EXISTS presupuesto (
                    id_presupuesto INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    monto REAL, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "ahorro": """
                CREATE TABLE IF NOT EXISTS ahorro (
                    id_ahorro INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    monto REAL, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "inversion": """
                CREATE TABLE IF NOT EXISTS inversion (
                    id_inversion INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    monto REAL, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "gasto": """
                CREATE TABLE IF NOT EXISTS gasto (
                    id_gasto INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    monto REAL, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "ingreso": """
                CREATE TABLE IF NOT EXISTS ingreso (
                    id_ingreso INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    monto REAL, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "porcentaje_acumulado": """
                CREATE TABLE IF NOT EXISTS porcentaje_acumulado(
                    id_porcentaje INTEGER PRIMARY KEY AUTOINCREMENT, 
                    cuenta INTEGER,
                    categoria INTEGER,
                    porcentaje REAL,
                    frecuencia TEXT, 
                    ultima_aplicacion DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(cuenta) REFERENCES cuenta(id_cuenta),
                    FOREIGN KEY(categoria) REFERENCES categoria(id_categoria),
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "estadistica_financiera": """
                CREATE TABLE IF NOT EXISTS estadistica_financiera(
                    id_estadistica INTEGER PRIMARY KEY AUTOINCREMENT, 
                    tipo TEXT, 
                    saldo_neto REAL, 
                    total_ingresos REAL,
                    total_gastos REAL,
                    periodo_inicio DATE,
                    periodo_fin DATE,
                    descripcion TEXT,
                    recomendacion TEXT, 
                    id_usuario INTEGER, 
                    porcentaje_gastado REAL,
                    porcentaje_ahorrado REAL,
                    porcentaje_invertido REAL,
                    porcentaje_deuda REAL,
                    porcentaje_ahorro REAL,
                    porcentaje_inversion REAL,
                    porcentaje_gasto REAL,
                    porcentaje_ingreso REAL,
                    porcentaje_presupuesto REAL,
                    porcentaje_ahorro_meta REAL,
                    porcentaje_inversion_meta REAL,
                    porcentaje_gasto_meta REAL,
                    porcentaje_ingreso_meta REAL,
                    porcentaje_presupuesto_meta REAL,
                    porcentaje_ahorro_acumulado REAL,
                    porcentaje_inversion_acumulado REAL,
                    porcentaje_gasto_acumulado REAL,
                    porcentaje_ingreso_acumulado REAL,
                    porcentaje_presupuesto_acumulado REAL,
                    porcentaje_ahorro_meta_acumulado REAL,
                    porcentaje_inversion_meta_acumulado REAL,
                    porcentaje_gasto_meta_acumulado REAL,
                    porcentaje_ingreso_meta_acumulado REAL,
                    porcentaje_presupuesto_meta_acumulado REAL,
                    FOREIGN KEY(recomendacion) REFERENCES recomendacion(id_recomendacion),
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,

    "meta_financiera": """
                CREATE TABLE IF NOT EXISTS meta_financiera (
                    id_meta INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    monto REAL, 
                    fecha_creacion DATE,
                    fecha_limite DATE,
                    descripcion TEXT, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """,
    "logro": """
                CREATE TABLE IF NOT EXISTS logro(
                    id_logro INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT,
                    descripcion TEXT, 
                    fecha_obtenido DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
            )
    """,
    "recomendacion": """
                CREATE TABLE IF NOT EXISTS recomendacion(
                    id_recomendacion INTEGER PRIMARY KEY AUTOINCREMENT, 
                    mensaje TEXT,
                    tipo TEXT, 
                    fecha DATE, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
            )
    """,
    "configuracion": """
                CREATE TABLE IF NOT EXISTS configuracion (
                    id_config INTEGER PRIMARY KEY AUTOINCREMENT, 
                    idioma TEXT, 
                    moneda TEXT, 
                    notificaciones BOOLEAN, 
                    id_usuario INTEGER, 
                    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
                )
    """
    }
    con = conectar() # se conecta a la base de datos 
    cur = con.cursor()
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas_existentes = set(row[0] for row in cur.fetchall())
    
    for nombre_tabla, sql in tablas_sql.items():
        if nombre_tabla not in tablas_existentes:
            print(f"Creando tabla: {nombre_tabla}")
            # Ejecuta la sentencia SQL para crear la tabla
            cur.execute(sql)
    
    con.commit()
    cur.close()
    # cierra el cursor
    con.close()

def crear_nueva_tabla(nombre_tabla):
    con = conectar()
    cur = con.cursor()
    
    # Crear una nueva tabla con un nombre específico
    query = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} (id_{nombre_tabla} INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)"
    cur.execute(query)
    
    con.commit()
    cur.close()
    con.close()
    
    print(f"Tabla {nombre_tabla} creada correctamente.")
    
def nuevo_columna_tipoDato_restricciones_tabla(nombre_tabla, nombre_columna, tipo_dato, restricciones):
    con = conectar()
    cur = con.cursor()
    
    # Agregar una nueva columna a la tabla con restricciones
    query = f"ALTER TABLE {nombre_tabla} ADD COLUMN {nombre_columna} {tipo_dato} {restricciones}"
    cur.execute(query)
    
    con.commit()
    cur.close()
    con.close()
    
    print(f"Columna {nombre_columna} agregada a la tabla {nombre_tabla} con restricciones: {restricciones}.")
    
def crear_nueva_tabla_desde_consola():
    nombre_tabla = input("Nombre de la nueva tabla: ")
    crear_nueva_tabla(nombre_tabla)

def agregar_nuevo_columna_tipoDato_restricciones_desde_consola():
    nombre_tabla = input("Nombre de la tabla: ")
    nombre_columna = input("Nombre de la nueva columna: ")
    tipo_dato = input("Tipo de dato (ejemplo: TEXT, INTEGER, REAL): ")
    restricciones = input("Restricciones (ejemplo: NOT NULL, UNIQUE): ")

    nuevo_columna_tipoDato_restricciones_tabla(nombre_tabla, nombre_columna, tipo_dato, restricciones)
    print(f"Columna {nombre_columna} agregada a la tabla {nombre_tabla} con restricciones: {restricciones}.")
    
def menu_creacion_tablas():
    while True:
        print("\nMenu de Creación de Tablas")
        print("1. Crear nueva tabla")
        print("2. Agregar nuevo valor/atributo con restricciones a una tabla")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_nueva_tabla_desde_consola()
        elif opcion == "2":
            agregar_nuevo_columna_tipoDato_restricciones_desde_consola()
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def verificar_tabla(nombre_tabla):
    con = conectar()
    cur = con.cursor()
    
    # Verificar si la tabla existe
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nombre_tabla,))
    if cur.fetchall():
            print(f"La tabla {nombre_tabla} existe.")
            cur.execute(f"SELECT * FROM {nombre_tabla}")
            filas = cur.fetchall()
            if filas:
                columnas = [desc[0] for desc in cur.description]
                print(" | ".join(columnas))
                for fila in filas:
                    print(" | ".join(str(valor) for valor in fila))
            else:
                print(f"La tabla {nombre_tabla} no contiene datos.")
    else:
        print(f"La tabla {nombre_tabla} no existe.")
    if not cur.fetchone():
        crear_tablas()
    
    cur.close()
    con.close()
    
    
def mostrar_tablas_y_datos(nombres_tablas):
    con = conectar()
    cur = con.cursor()
    
    for nombre_tabla in nombres_tablas:
        print(f"Tabla: {nombre_tabla}")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nombre_tabla,))
        if cur.fetchall():
            print(f"La tabla {nombre_tabla} existe.")
            cur.execute(f"SELECT * FROM {nombre_tabla}")
            filas = cur.fetchall()
            if filas:
                columnas = [desc[0] for desc in cur.description]
                print(" | ".join(columnas))
                for fila in filas:
                    print(" | ".join(str(valor) for valor in fila))
            else:
                print(f"La tabla {nombre_tabla} no contiene datos.")
        else:
            print(f"La tabla {nombre_tabla} no existe.")
    cur.close()
    con.close()

def revisar_columnas_existentes_todas_tablas(engine):
    inspector = inspect(engine)
    tablas = inspector.get_table_names()
    resultado = {}
    for tabla in tablas:
        columnas = inspector.get_columns(tabla)
        restricciones = inspector.get_pk_constraint(tabla)
        resultado[tabla] = {
            "columnas": [],
            "restricciones": restricciones
        }
        for columna in columnas:
            resultado[tabla]["columnas"].append({
                "nombre": columna["name"],
                "tipo": str(columna["type"]),
                "nullable": columna.get("default"),
                "autoincrement": columna.get("autoincrement")
                })
    return resultado
    
def menu_consultas():
    # Muestra un menú de consultas a la base de datos
    while True:
        print("\nMenu de Consultas")
        print("1. Ver todas las tablas")
        print("2. Consultar datos de una tabla")
        print("3. revisar parametro de las tablas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_tablas_y_datos(["usuario","categoria", "planta", "movimiento", "recomendacion", "metafinanciera", "logro", "configuracion", "estadistica_financiera", "porcentaje_acumulado", "ingreso", "gasto", "inversion", "ahorro", "presupuesto", "transacciones", "cuenta", "notificacion", "usuario_planta"])
        elif opcion == "2":
            nombre_tabla = input("Nombre de la tabla a consultar: ")
            verificar_tabla(nombre_tabla)
        elif opcion == "3":
            engine = conectar_engine()  # Asegúrate de que el engine esté conectado antes de usarlo
            resultado = revisar_columnas_existentes_todas_tablas(engine)
            for tabla, columna in resultado.items():
                print(f"Tabla: {tabla}")
                for col in columna["columnas"]:
                    print(f"  Columna: {col['nombre']}, Tipo: {col['tipo']}, Nullable: {col['nullable']}, Autoincrement: {col['autoincrement']}")
                print(f"  Restricciones: {columna['restricciones']}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida, intenta de nuevo.")
    
def actualizar_tabla(nombre_tabla, columna, nuevo_valor, condicion):
    con = conectar()
    cur = con.cursor()
  # ultima_actualizacion DATE DEFAULT(DATE('now'))  
    query = f"UPDATE {nombre_tabla} SET {columna} = ?, ultima_actualizacion = DATE('now') WHERE {condicion}"
    cur.execute(query, (nuevo_valor,))
    
    con.commit()
    cur.close()
    con.close() 
    
def actualizar_valor_desde_consola():
    nombre_tabla = input("Nombre de la tabla: ")
    columna = input("Nombre de la columna a actualizar: ")
    nuevo_valor = input("Nuevo valor: ")
    condicion = input("Condición para la actualización: ")

    actualizar_tabla(nombre_tabla, columna, nuevo_valor, condicion)
    print(f"Tabla {nombre_tabla} actualizada correctamente.")
    
def modificar_estructura_tabla(nombre_tabla, nueva_columna, tipo_dato):
    con = conectar()
    cur = con.cursor()
    
    query = f"ALTER TABLE {nombre_tabla} ADD COLUMN {nueva_columna} {tipo_dato}"
    cur.execute(query)
    
    con.commit()
    cur.close()
    con.close()
    
def modificar_estructura_desde_consola():
    nombre_tabla = input("Nombre de la tabla: ")
    nueva_columna = input("Nombre de la nueva columna: ")
    tipo_dato = input("Tipo de dato (ejemplo: TEXT, INTEGER, REAL): ")

    modificar_estructura_tabla(nombre_tabla, nueva_columna, tipo_dato)
    print(f"Estructura de la tabla {nombre_tabla} modificada correctamente.")
    
def menu_actualizacion():
    while True:
        print("\nMenu de Actualización de Tablas")
        print("1. Actualizar tabla")
        print("2. Modificar estructura de tabla")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            actualizar_valor_desde_consola()
        elif opcion == "2":
            modificar_estructura_desde_consola()
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            
def eliminar_tabla(nombre_tabla):
    con = conectar()
    cur = con.cursor()
    
    query = f"DROP TABLE IF EXISTS {nombre_tabla}"
    cur.execute(query)
    
    con.commit()
    cur.close()
    con.close()
    
def eliminar_tabla_desde_consola():
    nombre_tabla = input("Nombre de la tabla a eliminar: ")
    
    eliminar_tabla(nombre_tabla)
    print(f"Tabla {nombre_tabla} eliminada correctamente.")
    
def eliminar_valor_desde_consola():
    nombre_tabla = input("Nombre de la tabla: ")
    condicion = input("Condición para eliminar el valor: ")
    
    con = conectar()
    cur = con.cursor()
    
    query = f"DELETE FROM {nombre_tabla} WHERE {condicion}"
    cur.execute(query)
    
    con.commit()
    cur.close()
    con.close()
    
    print(f"Valor eliminado de la tabla {nombre_tabla} correctamente.")
    
def menu_eliminacion():
    while True:
        print("\nMenu de Eliminación de Tablas")
        print("1. Eliminar tabla")
        print("2. Eliminar valor de tabla")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            eliminar_tabla_desde_consola()
        elif opcion == "2":
            eliminar_valor_desde_consola()
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intenta de nuevo.")
 

def inicializar_base_datos():
    crear_tablas()
    # Inicializa la base de datos creando las tablas necesarias
    print("Base de datos inicializada correctamente.")
    
def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Consultas a la base de datos")
        print("2. Actualizacion de tablas")
        print("3. Eliminacion de tablas")
        print("4. Creacion de nuevas tablas")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_consultas()
        elif opcion == "2":
            menu_actualizacion()
        elif opcion == "3":
            menu_eliminacion()
        elif opcion == "4":
            menu_creacion_tablas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def main():
    inicializar_base_datos()
    menu_principal()

if __name__ == "__main__":
    main()