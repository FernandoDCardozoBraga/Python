print('Bienvenido al modulo de contrsseña segura')
contraseña = input('Favor ingrese su contraseña: ')

if len(contraseña) < 8:
    print('Contraseña demaciado corta, debe tener más de 8 caracteres')
else:
    minuscula = False
    for minus in contraseña:
        if minus.islower() == True:
            minuscula = True
    if not minuscula:
        print('La contraseña debe tener al menos una minuscula')
    
    mayuscula = False
    for mayus in contraseña:
        if mayus.isupper() == True:
            mayuscula = True
    if not mayuscula:
        print('La contraseña debe tener al menos una mayuscula')
    
    numero = False
    for carac in contraseña:
        if carac.isdigit() == True:
            numero = True
    if not numero:
        print('La contraseña debe tener al menos un número')
    
    if contraseña.count(' ') > 0:
        print('La contraseña no puede contener espacios en blanco')
    else:

        print('Contraseña Segura')




"""
Módulo de validación contraseñas de usuario en Python:

Ejercicio:
Crear un módulo de validación de contraseñas, este debe cumplir con los siguientes requisitos:
    - La contraseña debe contener mínimo 8 caracteres
    - Debe contener al menos; minúscula, mayúscula y números
    - No puede haber espacios en blancos en la contraseña
    - Si cumple con todos estos requisitos debe retornar el mensaje, «Contraseña segura»

Datos de entrada:
    - Contraseña

Proceso:
    - Validación de la longitud
    - Comprobación de mayúsculas y minúsculas
    - Comprobación de números y espacios

Datos de salida:
    - Si no cumple requisitos imprimir errores
    - Si cumple requisitos imprimir mensaje de contraseña segura
"""