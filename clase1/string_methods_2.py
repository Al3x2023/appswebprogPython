#otros metodos
from operator import indexOf

message='loscuervos de la utvt'
#len
size = len(message)
#replace
new_message = message.replace('',   '')
#find
index0f = message.find(' U')
#split
message_slice = message.split(' ')

print(f'Tamaño de la cadena{size}')
print('nueva cadena: {new_message}')
print(f'posicion del elemnto: {index0f}')
print(f'cadena{message_slice}')