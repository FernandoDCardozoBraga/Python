import random
print('Favorite Color')

color = input('Please type your favorite color: ')
print(f'Your favorite color is {color}')

print('Wait! Do you want to know curious facts about some colors?')
fact = input('please type yes or no: ')

if fact == ('yes'):
  colors=( ['rojo', 'amarillo', 'verde', 'azul', 'marrón', 'negro'])
  print (random.choice(colors))

else:
    print('OK, thank you!')
