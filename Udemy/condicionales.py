#revisar si una condicion es mayor a

balance = 500
if balance > 0:
    print('Puedes pagar')


    # if... else...

balance2 = 0
if balance2 > 0:
    print('Puedes pagar')
else:
    print('Saldo Insuficiente')


likes = 200
if likes == 200:
    print('excelente, 200 likes')

else:
    print('Casi llegas a los 200 likes')


likes = 199
if likes >= 200:
    print('excelente, 200 likes')

else:
    print('Casi llegas a los 200 likes')


#if con texto

lenguaje = 'Python'
if lenguaje == 'Python':
    print('Exelente decición')

# if not
                #la condicion no se cumple


lenguaje = 'Python'
if not lenguaje == 'Python':
    print('Exelente decición')

                # La condicion se cumple
        
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Exelente decición')


#evaluar un booleano

usuario_autenticado = True

if usuario_autenticado == True:
    print('acceso al sistema')
else:
    print('Debes iniciar sesión')