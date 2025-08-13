# Programa para convertir temperatura de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Entrada del usuario
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))

# Llamado a la función
resultado = celsius_a_fahrenheit(temperatura_celsius)

# Salida
print(f"{temperatura_celsius}°C es igual a {resultado:.2f}°F")