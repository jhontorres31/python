from random import *

aleatorioDecimal = uniform(1,5)
aleatorioInt = randint(1,5)
print(aleatorioInt)
print(aleatorioDecimal)

aleatorioOtro = random() #trae un decimal solo empieza en 0.

print(aleatorioOtro)

colores =[ 'rojo','azul','verde','amarillo']
aletorioColor = choice(colores)
print(aletorioColor)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

