# Formulario básico para capturar datos del usuario
nombre = input("Ingrese su nombre: ")  # Cadena (str)
edad = int(input("Ingrese su edad: "))  # Entero (int)
peso = float(input("Ingrese su peso en kg: "))  # Flotante (float)
es_estudiante = input("¿Es estudiante? (Sí/No): ").lower() == "sí"  # Booleano (bool)

# Mostrar los datos capturados
print("\nInformación del usuario:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Es estudiante: {'Sí' if es_estudiante else 'No'}")