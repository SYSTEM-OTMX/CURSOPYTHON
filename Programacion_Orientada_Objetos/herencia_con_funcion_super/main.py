from persona import Cliente, Empleado #importamos la subclase, en este caso cliente


print("*"*10)
empleado1 = Empleado('Alex',25,'pro',1500)
empleado2 = Empleado('Santos',23,'free',15555)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)


