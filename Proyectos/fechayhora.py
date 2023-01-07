#Obtener hora actual en python con el modulo time

import time

ahora = time.strftime("%c")
## representacion de fecha y hora
print("Fecha y hora " + time.strftime("%c"))

## representacion del tiempo
print ("Fecha "  + time.strftime("%x"))

## representacion de la hora
print ("Hora " + time.strftime("%X"))


"""
Los distintos formatos
Las siguientes directivas se pueden utilizar en el formato de cadena:

%a - Nombre del día de la semana
%A - Nombre del día completo
%b - Nombre abreviado del mes
%B - Nombre completo del mes
%c - Fecha y hora actual
%d - Día del mes
%H - Hora (formato 24 horas)
%I - Hora (formato 12 horas)
%j - Día del año
%m - Mes en número
%M- Minutos
%p - Equivalente de AM o PM
%S - Segundos
%U - Semana del año (domingo como primer día de la semana)
%w - Día de la semana
%W - Semana del año (lunes como primer día de la semana)
%x - Fecha actual
%X - Hora actual
%y - Número de año (14)
%Y - Numero de año entero (2014)
%Z - Zona horaria

"""

#Obtener la fecha y hora actual en Python usando el módulo datetime

import datetime

x = datetime.datetime.now()

print ("Fecha y hora = %s" % x)

print ("Fecha y hora en formato ISO = %s" % x.isoformat() )

print (u"Año = %s" %x.year)

print ("Mes = %s" %x.month)

print ("Dia =  %s" %x.day)

print ("Formato dd/mm/yyyy =  %s/%s/%s" % (x.day, x.month, x.year) )

print ("Hora = %s" %x.hour)

print ("Minutos = %s" %x.minute)

print ("Segundos =  %s" %x.second)

print ("Formato hh:mm:ss = %s:%s:%s" % (x.hour, x.month, x.second) )