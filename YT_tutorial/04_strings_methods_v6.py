#############################################
#############################################
####
#### Metodos de Formato
####
#############################################
#############################################

course = 'Curso'
my_string = 'Código Facilito!'

#Ejemplo 1
result = '{} de {}' .format(course, my_string)
print(f'Ejemplo 1 {result}')

#Ejemplo 2
result2 = '{a} de {b}' .format(a = course, b = my_string)
print(f'Ejemplo 2 {result2}')

#Ejemplo 3

result3 = '{a} de {b}' .format(a = course, b = my_string)
result3 = result3.lower()       #No modifica el strig original nos da otro string
print(f'Ejemplo 3 {result3}')


#Ejemplo 4

result4 = '{a} de {b}' .format(a = course, b = my_string)
result4 = result4.upper()       #No modifica el strig original nos da otro string
print(f'Ejemplo 4 {result4}')


#Ejemplo 5

result5 = '{a} de {b}' .format(a = course, b = my_string)
result5 = result5.title()       #No modifica el strig original nos da otro string
print(f'Ejemplo 5 {result5}')


#############################################
#############################################
####
#### Metodos de Busqueda
####
#############################################
#############################################

#Ejemplo 6

course6 = 'Curso'
my_string6 = 'Código Facilito!'


result6 = '{} de {}' .format(course6, my_string6)
position = result6.find('Código')

print(f'Ejemplo 6 {position}')


course7 = 'Curso'
my_string7 = 'Código Facilito!'

#Ejemplo 7
result7 = '{} de {}' .format(course7, my_string7)
count = result7.count('C')

print(f'Ejemplo 6 {count}')


#Ejemplo 8
course8 = 'Curso'
my_string8 = 'Código Facilito!'

result8 = '{} de {}' .format(course8, my_string8)
new_string = result8.replace('c', 'x')

print(f'Ejemplo 8 {new_string}')


#Ejemplo 9
course9 = 'Curso'
my_string9 = 'Código Facilito!'

result9 = '{} de {}' .format(course9, my_string9)
new_string9 = result9.split(' ')

print(f'Ejemplo 9 {new_string9}')


