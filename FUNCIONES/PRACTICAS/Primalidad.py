from tkinter.tix import Tree


def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        
        #verfica si se puede divir o no
        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False

def main():
    numero = int(input("INRESE UN NUMERO"))
    
    if es_primo(numero) == True:
        print("ES PRIMO")

    elif es_primo(numero) == False:
        print("NO ES PRIMO")


if __name__ == '__main__':
    main()