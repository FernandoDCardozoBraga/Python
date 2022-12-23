print('Calculadora de Indice de Masa Corporal (IMC)')

peso = float(input('Ingrese su peso en Kilogramos: '))
altura = float(input('Ingrese su altura en Metros: '))

imc = (peso/altura**2)

print(f'Su IMC es: {round(imc, 2)}, usted presenta: ')

if imc >= 0 and imc <= 15.99 :
    print ("Delgadez severa")
elif imc >= 16.00 and imc <= 16.99 :
    print ("Delgadez moderada")
elif imc >= 17.00 and imc <= 18.49:
    print ("Delgadez leve")
elif imc >= 18.50 and imc <= 24.99 :
    print (" Peso Normal")
elif imc >= 25.00 and imc <= 29.99:
    print ("Sobrepeso")
elif imc >= 30.00 and imc <= 34.99:
    print ("obesidad leve")
elif imc >= 35.00 and imc <= 39.00:
    print ("obesidad media")
elif imc >= 40.00:
    print ("obesidad morbida")

