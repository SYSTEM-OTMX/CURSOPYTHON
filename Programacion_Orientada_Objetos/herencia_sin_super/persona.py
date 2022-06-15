class Persona: #esta es la clase personal o super clase
    def __init__(self, nombre, edad, cuenta):
        self.nombre = nombre
        self.edad = edad
        self.cuenta = cuenta

    def detalle_persona(self):
        print(f' Nombre :{self.nombre} \nEdad :{self.edad} \nCuenta :{self.cuenta}')

    def __str__(self):
        return f' Nombre :{self.nombre} \nEdad :{self.edad}\nCuenta :{self.cuenta}'

#clase cliente que hereda de persona
class Cliente(Persona): #subclase poniendo entre parentesis el nombre de la clase a heredar

    pass

#clase cliente que hereda de persona
class Empleado(Persona):
    def __init__(self, nombre, edad, cuenta, sueldo):
        #heredar constructor de la funcion persona osea clase padre para ello se usa super
        #super().__init__(nombre, edad, cuenta)
        #heredar sin super
        Persona.__init__(self,nombre,edad,cuenta)
        #instancioar sueldo
        self.sueldo = sueldo

    def detalle_empleado(self):
        #heredar estado de objeto de la clase persona
        #super().detalle_persona()
        #heradar sin super
        Persona.detalle_persona(self)
        #se agrega la ultima instancia que es sueldo
        print('Sueldo: ',self.sueldo)

    def __str__(self):
        #nuevamente con super heredamos el estado de objeto de la clase padre 
        #super().__str__() + f'\Sueldo: {self.sueldo}'
        #Heredar sin super
        return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'