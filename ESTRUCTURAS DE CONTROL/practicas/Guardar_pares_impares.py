
#Creacion de tupla 
import random


tupla = (1,2,3,4,5,6,7,8,9)

#Creacion de lista de pares
pares = []

#Creacion de lista de impares
impar = []

for dato in tupla:
    nran = random.randint(1,100)

    resultado = dato * nran

    print(dato," X ",nran," = ",resultado)

    if resultado % 2 == 0:
        pares.append(resultado)
    else:
        impar.append(resultado)

print("*"*30)
print("PARES")
print(pares)
print("*"*30)
print("IMPARES")
print(impar)
print("*"*30)
