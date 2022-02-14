
#modulo de fibonacci

def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')#IMPRIMIR CADA ITERACION EN LA MISAM LINEA
        a, b = b, a + b #1 + 1 = 2, 2 + 1etc 


    print()


def fibo2(n):
    resultado = []
    a, b = 0, 1
    while a < n:
        resultado.append(a)
        a, b = b, a + b #1 + 1 = 2, 2 + 1etc 


    return resultado

    

