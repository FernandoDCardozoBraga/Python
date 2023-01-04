########################
#
#Ejemplo 0 y 1
#
########################
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
print(f'ejemplo 0 {lenguajes}')
print(f'ejemplo 1 {lenguajes[0]}')  #Los arrays list comienzan en la posicion 0


########################
#
#Ejemplo 2
#
########################

#ordenar los elementos (alfabeticamente)
lenguajes.sort()
print(f'ejemplo 2 {lenguajes}')

########################
#
#Ejemplo 3
#
########################

#acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(f'ejemplo 3 {aprendiendo}')


########################
#
#Ejemplo 4
#
########################

#Modificar valores de un arreglo

lenguajes[2] = 'PHP'
print(f'ejemplo 4 {lenguajes}')

########################
#
#Ejemplo 5
#
########################

#agregar elementos a un arreglo

lenguajes.append('Ruby')
print(f'ejemplo 5 {lenguajes}')

########################
#
#Ejemplo 6
#
########################

#eliminar de un arreglo

del lenguajes[1]
print(f'ejemplo 6 {lenguajes}')

########################
#
#Ejemplo 7 y 8 .pop
#
########################


#eliminar el ultimo elemento de un arreglo

lenguajes.pop()
print(f'ejemplo 7 {lenguajes}')

#eliminar con pop un elemento especifico

lenguajes.pop(0)
print(f'ejemplo 8 {lenguajes}')



########################
#
#Ejemplo 9 .remove
#
########################


lenguajes.remove('PHP')
print(f'ejemplo 9 {lenguajes}')