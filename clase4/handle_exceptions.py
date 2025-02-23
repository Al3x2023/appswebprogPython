result=None

numero_x=10
numero_y=1
try:

    result=numero_x/ numero_y
    print(f'El resultado de la divicion es:{result}')
except ZeroDivisionError as e:
    print(f'La excepción es la equivalente:{e}')
finally:
    print('Nuestro programa ha finalizado')
