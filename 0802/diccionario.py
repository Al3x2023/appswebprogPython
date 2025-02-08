# Declarar un diccionario en Python
student = {
    'name': 'Pedrito Perez',
    'age': 25,
    'language': 'python',
    'city': 'lerma',
}

# Acceso a los valores de un diccionario
print(f'Contenido total del estudiante: {student}')
print(f'Nombre: {student["name"]}')
print(f'Edad: {student.get("age")}')

print('\n...Operaciones básicas sobre diccionarios...')
# Modificar los valores de un diccionario
student['language'] = 'C#'
print(f'Contenido actual del estudiante: {student}')

# Eliminar un elemento de un diccionario
student.pop('city')
print(f'Contenido del estudiante una vez eliminada la ciudad: {student}')

# Agregar un nuevo elemento
student['food'] = 'galletas'
print(f'Contenido del estudiante una vez agregada una nueva propiedad: {student}')

print('\n--- Iterar sobre un diccionario ---')
print('\nIteración de los elementos de un diccionario (simple)')

for element in student:
    print(f'{element}: {student[element]}')

print('\nIteración de los elementos de un diccionario (desestructuración - unpacking)')

for key, value in student.items():
    print(f'Llave: {key}, Valor: {value}')

print('\nIteración de los elementos de un diccionario (Llaves)')

for key in student.keys():
    print(f'Llave: {key}')

print('\nIteración de los elementos de un diccionario (Valores)')
for value in student.values():
    print(f'Valor: {value}')
