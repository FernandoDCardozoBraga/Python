
pan_fresco = 3.49
descuento = 0.6

cantidad_pan = int(input('Ingrese la cantidad del día anterior a vender: '))
print(f'El coste barra de pan fresco: {pan_fresco}€')
print('Descuento:' + str(descuento*100) +'%')
coste = (cantidad_pan*pan_fresco*( 1 - descuento))
print(f'Coste final Pan con descuento: {round(coste, 2)}€')