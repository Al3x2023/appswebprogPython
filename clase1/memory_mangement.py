number_x=10
number_y=20
address_x_id=id(number_x)
address_y_id=id(number_y)
print('**Antes de actualizar el valor de x**')
print(address_x_id)
print(address_y_id)
number_x=20
address_x_id=id(number_x)
print('\n**Despues de actualizar el valor de x**')
print(address_x_id)
print(address_y_id)