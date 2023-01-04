
my_strings = 'Hola Mundo! "Fernando"'
print(my_strings)

#string con salto de linea
my_strings_two = """Una de las mayores curiosidades de este color es su nombre…\n
Y es que el naranja se conocía en Europa como amarillo rojizo hasta el siglo XVI.\n
Esto cambió con la llegada de los naranjos provenientes de Asia, 300 años después\n
de su llegada, esta tonalidad adoptó el nombre de la fruta."""
print(my_strings_two)


course = 'Python 3'
name = 'Fernando'
final_message = course + name   #0
print(final_message)


course_a = 'Python 3'
name_a = 'Fernando'
final_message_two = 'Bienvenido ' + name_a + ' al curso de ' + course_a +'.'  #1
print(final_message_two)

course_b = 'Python 3'
name_b = 'Fernando'
final_message_three = 'Bienvenido  %s al curso de %s' %(name_b, course_b)+' metodo 2'  #2
print(final_message_three)

course_c = 'Python 3'
name_c = 'Fernando'
final_message_four = 'Bienvenido  {} al curso de {}' .format(name_c, course_c)+' metodo 3'  #3
print(final_message_four)