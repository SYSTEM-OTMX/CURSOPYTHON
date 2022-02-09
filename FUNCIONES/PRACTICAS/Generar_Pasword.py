import random

def generador_password():
    mayusculas = ['A','B','C','D','F','G']
    minuscula = ['a','b','c','d','f','g']
    sinmoblos = ['#','$','%','&','/','!']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minuscula + sinmoblos + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)#sacar un elemetno aleratorio de una lista
        password.append(caracter_random)

    password = "".join(password)#convertir lista en un cadena de carateres.
    
    return password

def main():

    password = generador_password()

    print("*"*30)
    print(" "*30)
    print("PASSWORD GENERADO :", password)


if __name__ == "__main__":
    main()