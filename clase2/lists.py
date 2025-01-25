print(f'Valores modificados de mi lista: {my_list}')

# Ordenar los elementos de mi lista mediante SORT
my_list.sort()

print(f'Los elementos de mi lista han sido ordenados: {my_list}')
# Modificar y eliminar un elemento de mi lista
my_list[0] = 'Esta es una cadena'
my_list.pop()

print(f'Valores actuales de mi lista, ejemplo POP: {my_list}')
# Creación de una sublista
my_sublist = my_list[0:5]
print(f'Valores actuales de mi sublista: {my_sublist}')

# Imprimir los valores de mi lista
print(f'\nEstos son los elementos de mi lista, los cuales serán impresos mediante un ciclo for')
count = 0
for item in my_list:
    print(f'Elemento de mi lista {count}: {item}')
    count += 1
