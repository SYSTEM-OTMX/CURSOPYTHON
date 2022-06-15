class Persona: #esta es la clase personal o super clase
    def __init__(self, nombre, edad, cuenta):
        self.nombre = nombre
        self.edad = edad
        self.cuenta = cuenta

    def detalle_persona(self):
        print(f' Nombre :{self.nombre} \nEdad :{self.edad} \nCuenta :{self.cuenta}')

    def __str__(self):
        return f' Nombre :{self.nombre} \nEdad :{self.edad}\nCuenta :{self.cuenta}'


class Cliente(Persona): #subclase poniendo entre parentesis el nombre de la clase a heredar

    pass