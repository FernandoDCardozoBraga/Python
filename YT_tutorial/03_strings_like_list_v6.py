my_string = 'Curso de código facilito!'
print(my_string [0])    # Para tratar a un string como lista se debe agregar []


#Para recorer el string de derecha a izquierda dentro de los parentesis [] necesitamos poner un numer negativo

my_string1 = 'Curso de código facilito!'
print(my_string1 [-1])

#Si deseo saber cuales son los caracteres de cada extremo

my_string2 = 'Curso de código facilito!'
print(my_string2 [0], my_string2 [-1])


#Si deseo mostrar una "sublista" superstring dentro de mi string
#debo colocar de donde debo comemenzar seguido de 2 puntos : // seguido del indice donde quiero terminar

my_string3 = 'Curso de código facilito!'
print(my_string3 [0:10])

# Con las listas podemos hacer saltos progresivos

my_string4 = 'Curso de código facilito!'
print(my_string4 [0:10:2])


#Leer un string de derecha a izquierda

my_string5 = 'Curso de código facilito!'
print(my_string5 [::-1])

