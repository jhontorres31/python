def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

    #sum(args)


print(suma(5,6,7,1,500))