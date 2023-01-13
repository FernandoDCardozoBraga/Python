#Las listas son un tipo de dato que a diferencia de los enteros y los strings pueden almacenar diferentes tipos de datos
# a dferencia de los strings y los enteros las listas si pueden modificar su tamaño.

#Ejemplo 1

my_list = ['srings', 15, 15.6, True]
print(my_list)

#Ejemplo 2

my_list = ['srings', 15, 15.6, True]
my_list.append(6)           #append recibe como parametro el elemento introducido dentro de los parentesis y lo va a agregar
print(my_list)              # a la lista en la ultima posision 
                            
#Ejemplo 3

my_list = ['strings', 15, 15.6, True]
my_list.insert(1, 'insert')    # insert a diferencia de append recibe dos tipos de datos el primero que indica la posicion donde
print(my_list)                 #será ingresado el dato


# Las listas tambiaen estan sujetas al index  y se comprtan igual a un string

#Ejemplo 4
my_list = ['strings', 15, 15.6, True]
print(my_list [1])


#Ejemplo 5

my_list = ['strings', 15, 15.6, True]
my_list.remove(15)
print(my_list)    


#Ejemplo 6

my_list = ['strings', 15, 15.6, True]
my_list.pop()
print(my_list)    #toma el ultimo parametro y lo elimina de la lista


#Ejemplo 7
#Ordenar

my_list = [1, 9, 22, 6, 8, 65, 14, 99]
my_list.sort()
print(my_list)


#Ejemplo 7b
my_list = [1, 9, 22, 6, 8, 65, 14, 99]
my_list.sort(reverse = True)  #sort puede recibir como parametro reverse = true para ordenar de forma decendente
print(my_list)


#Ejemplo 8 unir listas

my_list = [1, 9, 22, 6, 8, 65, 14, 99]
my_list2 = [22, 45, 15, 7, 2]

my_list.extend(my_list2)
print(my_list)

#No es lo mismo utilizar append ya que el resultado es una lista dentro de otra liasta

my_list = [1, 9, 22, 6, 8, 65, 14, 99]
my_list2 = [22, 45, 15, 7, 2]

my_list.append(my_list2)
print(my_list)