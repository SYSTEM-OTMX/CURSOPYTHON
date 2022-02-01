
#Una funcion recursiva es aquella que se repite a si misma
#sacar un factorial

def factorial(n):
    print('Valor incial:',n)
    if n > 1:
        n = n * factorial(n - 1)
    print('Valor final:',n)
    return n

print("INGRESE UN NUMERO")
n = int(input())

f = factorial(n)

print(f)