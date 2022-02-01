
#condicional simple

from click import progressbar


if False:
    print("SE CUMPLE LA CONDICION")
else:
    print("NO SE CUMPLIO LA CONDICION")

    n = int(input("INGRES UN NUMERO ENTERO"))

    if n % 2 == 0:
        print("ES UN NUMERO ENTERO")

    else:
        print("EL NUMERO ES INPAR")


#condicional anidado



n = int(input("INGRES UN NUMERO ENTERO"))

if n != 0:
    # pass sirve para decir que no se va hacer nada por el momento

    if n > 0:
        print("EL NUMERO ES POSITIVIO")
        if n % 2 == 0:
            print("ES UN NUMERO PAR")

        else:
            print("EL NUMERO ES INPAR")

    else:
        print(f"EL NUMERO {n} ES NEGATIVO")
        if n % 2 == 0:
            print("ES UN NUMERO PAR")

        else:
            print("EL NUMERO ES INPAR")
else:
    print(f'EL NUMERO {n} ES NEUTRO')
    
