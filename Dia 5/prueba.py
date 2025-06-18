def suma_cuadrados(*args):
    total=0
    for arg in args:
        cuadrado=0
        cuadrado = arg * arg

        total += cuadrado

    return total


print(suma_cuadrados(2, 3, 5))


def suma_absolutos(*args):
    total=0
    for arg in args:

        if (arg < 1):
           arg= arg * -1

        total += arg

    return total


print(suma_absolutos(1, -2, 4, -5))

'''Práctica sobre Argumentos Indefinidos (*args) 3

Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, 
y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"'''


def numeros_persona (*args):

    lista=[]
    suma=0
    for arg in args:
        lista.append(arg)
        if type(arg)==int:
            suma +=arg

    return print(f"{lista[0]}, la suma de tus numeros es {suma}")

numeros_persona('Jhon',1,3,5,7)








