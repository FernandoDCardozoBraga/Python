#Nos permiten almacenar distintos tipos de datos pero a diferencias de las listas no pueden ser modificadas (agregar o quitar elementos)

my_tuple = (1, 'string', True)
print(my_tuple)


#Para acceder a una posicion dentro de la tupla

my_tuple = (1, 'string', True)
print(my_tuple[0])

#Lo aplicable a strings y listas se puede aplicar a las tuplas. No podemos quitar y/o agregar

# Se usa una tupla cuando siemple que se nececite un control total sobre las diferentes tipos de datos y que los mismos sean constante
# Ej: password de una base de datos que no sera modificado, una ruta especifica, permisos etc. ya que no seran moficados en el transcurso del proyecto.
