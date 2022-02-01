from doctest import REPORTING_FLAGS


c = 0

while c < 10:
    c += 1
    print(c)
    if c == 2:
        print("SALTANDO DE CASILLA")
        continue # AL CONTRARIOP QUE BREACK SOLO SAALTA A LA SIGUIENTE INTERACION ES DECIR EL SIGUIENTE BUCLE
    print("DESPUES DEL CONTINUE")

    if c == 5:
        print("terminando el blucle del programa")
        break # romper el ciclo cuando c tenga valor de 5


else:
    print("FIN DEL WHILE")