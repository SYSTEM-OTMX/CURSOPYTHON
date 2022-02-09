







def main ():
    print("*"*30)
    print(" "*30)
    print("INGRESE PALABRA:")
    palin = str(input())
    print(" "*30)
    print("*"*30)
    print(" "*30)
    print("PALABRA INGRESADA : ",palin.upper())
    print(" "*30)
    print("*"*30)

    verificar(palin)


#funcion de entrada de la aplicacion


def verificar(palabra):

    palabra.replace(' ','')
    palabra.lower()
    revertir = palabra[::-1]

    if revertir == palabra:
        print(" "*30)
        print(f"LA PALABRA {palabra.upper()} ES UN PALINDROMO")
        print(" "*30)
        print("*"*30)
    else:
        print(" "*30)
        print(f"LA PALABRA {palabra.upper()} NO ES UN PALINDROMO")
        print(" "*30)
        print("*"*30)

if __name__ =='__main__':
    main()
