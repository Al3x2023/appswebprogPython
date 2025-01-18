# If statement - elif
age = int(input('¿Cuál es tu edad? '))

if age <= 12:
    print('Eres un niño')
elif age <= 18:
    print('Eres un adolescente')
elif age <= 35:
    print('Eres un adulto joven')
else:
    print('Eres un adulto')
