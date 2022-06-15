from persona import Cliente #importamos la subclase, en este caso cliente


cliente1 = Cliente('Eduardo',25,'pro')
cliennte2 = Cliente('santos', 25,'free')
cliennte3 = Cliente('luis ', 25,'pro')
cliente1.detalle_persona()#ejecuta el metodo de mostrar datos


print(cliente1)#imprime el estado del objeto llamaod __str__
print(cliennte2)
print(cliennte3)