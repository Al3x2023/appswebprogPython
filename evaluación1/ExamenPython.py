# Solicitar nombre al usuario
nombre = input("Ingresa tu nombre: ")

# Solicitar el número de materias
num_materias = int(input("Ingresa el número de materias: "))

# Inicializar una lista para almacenar las calificaciones
calificaciones = []

# Solicitar las calificaciones de cada materia
for i in range(1, num_materias + 1):
    calificacion = float(input(f"Ingrese la calificación de la materia #{i}: "))
    calificaciones.append(calificacion)

# Calcular el promedio
promedio = sum(calificaciones) / num_materias

# Imprimir el resultado
print(f"\n{nombre} El promedio de su cuatrimestre: {promedio:.2f}")
