
nombres = ['juan', 'carlos', 'ana']

for elemento in nombres:
    print('Hola ' + elemento)

lista = ['a','b','c','d']
print('\n')
for letra in lista:
    numero_letra = lista.index(letra) +1
    print(f"letra {numero_letra}: {letra} ")

lista1 = ['pablo', 'luis', 'laura', 'fede', 'julia']
print('\n')
for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')
print('\n')
numeros =[1,2,3,4,5]
miValor = 0

for numero in numeros:
    miValor = miValor + numero
    print(miValor)
print('\n')
palabra = 'python'

for letrass in palabra:
    print(letrass)
print('\n')
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print('\n')

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for a,b in dic.items():
    print(a,b)