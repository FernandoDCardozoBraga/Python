print('Calculadora de Interes Compuesto')

c = float(input('Ingrese capital inicial: '))
i = 4
n = 1
n1 = 2
n2 = 3

m = (c*(1 + (i/100))**n)
m1 = (c*(1 + (i/100))**n1)
m2 = (c*(1 + (i/100))**n2)

print(f'El interés compuesto sobre $UYU {c} al {i}% anual: \n Durante {n} año corresponde a: $UYU {round(m, 2)} \n Durante {n1} años corresponde a: $UYU {round(m1, 2)} \n Durante {n2} años corresponde a: $UYU {round(m2, 2)}')

"""
En términos generales, el monto compuesto se puede escribir como:



M = C × (1 + i)n​

Fórmula de monto de capital más intereses calculados como interés compuesto​

Donde:

M es la suma de capital más intereses al final del período.

C es el capital inicial.

i es la tasa de interés compuesto.

n es el número de períodos durante los cuales se capitaliza el interés compuesto.

https://usuariofinanciero.bcu.gub.uy/Paginas/Tasas_Formula2.aspx

"""