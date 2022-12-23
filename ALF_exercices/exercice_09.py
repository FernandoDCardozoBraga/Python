payasos = 112
muñeca = 75
cantidad_payaso = int(input('Ingrese la cantidad de payasos a despachar: '))
cantidad_muñeca = int(input('Ingrese la cantidad de muñecas a despachar: '))
logistica = ((payasos*cantidad_payaso) + (muñeca*cantidad_muñeca))
print(f'Peso total del paquete que será enviado: {logistica} gramos')