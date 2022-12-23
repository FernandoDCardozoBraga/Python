print('Calculadora de enteros')

dividendo = int(input('Ingrese número ENTERO a dividir: '))
divisor = int(input('Ingrese número ENTERO como divisor: ' ))

cociente = (dividendo / divisor)
resto = (dividendo % divisor)

print(f'{dividendo} entre {divisor} da un cociente {cociente} y un resto {resto}')