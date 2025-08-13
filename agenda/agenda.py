# Sistema de agenda de contactos utilizando un diccionario
agenda = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    email = input("Ingrese el correo electrónico del contacto: ")
    agenda[nombre] = {"Teléfono": telefono, "Email": email}
    print(f"Contacto {nombre} agregado exitosamente.")

def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre, detalles in agenda.items():
            print(f"\nNombre: {nombre}")
            print(f"Teléfono: {detalles['Teléfono']}")
            print(f"Email: {detalles['Email']}")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"\nContacto encontrado:")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['Teléfono']}")
        print(f"Email: {agenda[nombre]['Email']}")
    else:
        print(f"No se encontró ningún contacto con el nombre {nombre}.")

# Menú principal
while True:
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        print("Saliendo de la agenda. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")