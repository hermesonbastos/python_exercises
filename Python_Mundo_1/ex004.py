# Oferecer o máximo de informações sobre uma variável

a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}' .format(type(a)))
print('Só tem espaços ?', a.isspace())
print('É um número ?', a.isnumeric())
print('É alfabético ?', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('Está em maiúsculo ?', a.isupper())
print('Está em minúsculo ?', a.islower())
print('Está capitalizada ?', a.istitle())