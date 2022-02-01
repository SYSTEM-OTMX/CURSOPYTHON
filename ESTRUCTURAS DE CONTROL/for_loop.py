from pickle import TRUE


datos = ['EDAUARDO',12,1.6,True]


print("IMPRECION DE LISTA USANDO FOR")

for dato  in datos:
    print(dato)


print("IMPRECION DE DATOS LISTAA CON WHILE")

c = 0

while c < len(datos):

    print(datos[c])
    c += 1

print("IMPRIMIR LISTA DE NUEMRO DEL 0 AL 10")

for n in range(10):
    print("DATO:",n)

    n += 1



print("IMPRIMIR LISTA DE NUEMRO DEL 10 AL 20")

for n in range(10,20):
    print("DATO:",n)

    n += 1
