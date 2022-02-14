import random

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elegido = None


    while numero_random != numero_elegido:
        numero_elegido = int(input("INRESE NUMERO ENTRE 1 Y 100:"))

        if numero_random < numero_elegido:
            print("ELIGE UN NUMERO MENOR")
            vidas -= 1

        elif numero_random > numero_elegido:
            print("ELIGE UN NUMERO MAS GRANDE")
            vidas -= 1

        if vidas == 0:
            print("FIN DEL JUEGO")
            break

        print(f'TE QUEDAN {vidas} vidas')

    if numero_elegido == numero_random:
        print("FELICIDADES GANASTE")


def main():
    print("INGRESE NUMERO DE VIDAS")
    vidas = int(input())
    jugar(vidas)



    
if __name__ == "__main__":
    main()