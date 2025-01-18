# Entrada de datos mediante la consola INPUT
name = input('¿Cuál es tu nombre? ')
age = int(input('¿Cuál es tu edad? '))
salary = float(input('¿Cuál es tu salario? '))
total_pets = eval(input('¿Cuántas mascotas tienes? '))
university = input('¿Cuál es el nombre de tu Universidad? ')

print(f'Hola, me llamo {name}, mi edad es {age}, mi salario es {salary}, tengo {total_pets} mascotas y mi universidad es {university}.')
print(type(name))
print(type(age))
print(type(salary))
print(type(total_pets))
