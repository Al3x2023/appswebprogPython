# Función sin argumentos
def saludar():
    print("Hola mundo desde una función")

# Función para sumar dos números
def sumar_numeros(numero_x, numero_y):
    suma = numero_x + numero_y
    print(f"El resultado de la suma es: {suma}")
    return suma

# Llamada a la función sumar_numeros
sumatoria = sumar_numeros(numero_x=10, numero_y=20)
print(f'El valor de la sumatoria es: {sumatoria}')

# Función con valores por defecto
def valores_por_defecto_suma(numero_x=0, numero_y=1, numero_z=2):
    suma = numero_x + numero_y + numero_z
    print(f"El resultado de la suma con valores por defecto es: {suma}")
    return suma

# Función con *args (argumentos variables)
def alumnos_materias(nombre, *args):
    print(f'Nombre: {nombre}, Materias: {args}')
    print(f'Tipo de nombre: {type(nombre)}, Tipo de materias: {type(args)}')

# Función con **kwargs (diccionario de argumentos)
def alumnos_calificaciones(nombre, **kwargs):
    print(f'Nombre: {nombre}, Calificaciones: {kwargs}')
    print(f'Tipo de nombre: {type(nombre)}, Tipo de calificaciones: {type(kwargs)}')

# Llamada a la función alumnos_calificaciones
alumnos_calificaciones(nombre="Josesito", programacion=10, matematicas=9, ingles=10)
