from itertools import count


b = ("hola").upper#convertir a mayuscula
b = ("hola").lower#convertir a minuscula
b = ("hola").capitalize#convertir el primer caracter en mayuscual
b = ("hola").title#Mayuscula cada primer caracter de cada palabra
b = ("hola").count('o')#contar cuantos caracteres existen en una cadena
b = ("hola")
b = b.replace('h','s')#reemplazar algun caracter de una cadena
b = ("   hola   ").strip()#eliminar espacios al pricipio o al final
b = ("--------hola-------").strip('-')#eliminar algun caracter en especial al principo o final

b = ("hola").split()#convertir cadena en lista
b = ("hola").split(',')#convertir cadena en lista con separacion en especial
b = ("hola").islower()#saber si la canena es minuscula
b = ("hola").isupper()#saber si la cadena es mayuscula
b = ("hola").istitle()#saber si la cadena es de tipo titulo
b = ("     ").isspace()#saber si la cadena es de puros espacios