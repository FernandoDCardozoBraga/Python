from string import punctuation

def validador_contrasenia (cts) :

    if 5 < len(cts) < 13:
        if any ([c.isdigit() for c in cts]):
            if any ([c.islower() for c in cts]):
                if any ([c.isupper() for c in cts]):
                    if any ([True if c in punctuation else False for c in cts]):
                        print ('contraseña establecida correctamente')
                        return True
                    else:
                        print('La contraseña ha de contener algún caracter especial')
                else:
                    print('La contraseña debe contener alguna mayúscula')
            else:
                print('La contraseña debe contener alguna minúscula')
        else:
            ('La contraseña debe contener algún dígito')
    else:
        print('La contraseña a de tener entre 6 y 12 caracteres')
    return False

intentos = 0

while True:
    contrasenia = input('Ingrese su Contraseña: ')
    intentos +=1

    if validador_contrasenia(contrasenia):
        print('La contraseña introducida ha sido {}' .format(contrasenia))
        break
    elif intentos > 5:
        contrasenia = None
        print('No se ha sido posible establecer una contraseña')
        break