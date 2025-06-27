"""
Modulo dedicado a la aplicacion, todo converge y se usa aqui
"""

import services
import models
import hashlib

def app():
    while True:
        # Menú principal: muestra opciones de inicio de sesión, registro y salida y espera la respuesta del usuario
        option = input("""Opciones disponibles:
            1. Sing in.
            2. Login.
            3. Exit.
            
Tu opcion: """)
            
        match option:
            case "1":
                # opción para iniciar sesión
                print("Iniciar seccion")
                email =  input("Tu correo electronico: ")
                contrasena = input("Contraseña: ")
                inicio_de_seccion = services.iniciar_seccion(email, contrasena)
                if inicio_de_seccion:
                    print("Bienvenido a casa!")
                    eleccion_usuario = input("""Esto es lo que puedes hacer en la aplicacion: 
                    1. Registrar gasto
                    2. Registrar ingreso
                    3. Registrar cuenta
                    4. Ver estadisticas de la cuenta
                    5. Establecer meta financiera
                    6. Ver estadisticas de tu planta
                    7. 
            """)

            case "2":
                # opción para registrarse
                print("Registrarse")
                while True:
                    nombre = input("Nombre de usuario: ")
                    email = input("Tu correo electronico: ")
                    contrasena = input("Contraseña: ")
                    # Se encripta la contraseña antes de guardarla
                    hash_obj = hashlib.sha256(contrasena.encode())
                    hash_hex = hash_obj.hexdigest()
                    usuario_registrado = services.registrar_usuario(models.Registrar_usuario(nombre, email, hash_hex))
                    
                    if usuario_registrado[0]:
                        print("""      
          ¡Bienvenido! a Finan Planta!
Porfavor ingresa los siguientes datos para saber mas de ti:
""")
                        # Solicita el monto actual del usuario
                        try:
                            monto = float(input("¿Cuanto dinero tienes actualmente?: "))
                            print("""Ya veo, con tu saldo actual puedes acceder a las siguientes plantas financieras: """)
                        except ValueError:
                            print("Porfavor ingresa un monto valido.")
                            continue
                        # Llama al menu inicial de cuenta nueva
                        services.menu_inicial_cuenta_nueva(usuario_registrado[1], monto)
                        break
                    else:
                        print("Registro invalido")
            case "3":
                # opción para salir
                print("Saliendo de la aplicacion.")
                break
            case _:
                # Maneja cualquier otra opción no válida
                print("Opcion no valida.")

if __name__ == "__main__":
    # Punto de entrada de la aplicación
    print("Bienvenido a Finan Planta!")
    app()
