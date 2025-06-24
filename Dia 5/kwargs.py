def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        #print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(x=3, y=5, z=2))


def suma2(num1, num2, *args, **kwargs):#Este es el orden en que se deben suministrar

    print(f"el primer numero es {num1}")
    print(f'el segundo numero es {num2}')

    for arg in args:
        print(f"arg:{arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")



suma2(15,30,100,200,300,x=20,y=40,z=50)

