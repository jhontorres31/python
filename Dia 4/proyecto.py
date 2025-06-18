from random import *

numeroIngresado=0
nombreUsuario = input('Digite su nombre: ')

print(f"Bueno, {nombreUsuario}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

intentos = 8
numeroAleatorio = randint(1,100)

for intentos in range(intentos):
    numeroIngresado = int(input('ingresa un numero: '))

    if numeroIngresado < 1 or numeroIngresado > 100:
        print('el numero es incorrecto')
    elif numeroIngresado<numeroAleatorio:
        print('Respuesta incorrecta, ha elegido un numero menor al correcto')
    elif numeroIngresado>numeroAleatorio:
        print('Respuesta incorrecta, ha elegido un numero mayor  al correcto')
    else:
        print(f'{nombreUsuario}ha ingresado el numero correcto te ha costado {intentos+1} intentos ')
        break
if numeroAleatorio != numeroIngresado:
    print(f'Lo siento {nombreUsuario}, se han agotado los intentos. El numero secreto es {numeroAleatorio}')