result=None

numero_x=10
numero_y=1
try:

    numero_x=int(input('Ingrese un numero para X: '))
    numero_y=int(input('Ingrese un numero para Y: '))
   
    result=numero_x/ numero_y

    print(f'El resultado de la divicion es:{result}')
except ZeroDivisionError as e:
    print(f'La excepción es la equivalente:{e}')
except ValueError as e:
    print(f'La excepción ValueError genero el siguinte mensaje:{e}')
except Exception as e:
    print(f'La excepción Exception genero el siguinte mensaje:{e}')
finally:
    print('Nuestro programa ha finalizado')
