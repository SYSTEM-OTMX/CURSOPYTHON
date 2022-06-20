class Figura:
    def __init__(self,nombre,base,altura) :
        self.nombre = nombre
        self.base = base
        self.altura = altura

    def area(self):
        print("")
    def perimetro(self):
        print("")

class Rectangulo(Figura):
    def __init__(self,nombre,base,altura) :
        super().__init__(nombre,base,altura)
        super().area(base,altura)
        super().perimetro()
    
    pass

class Circulo(Figura):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre,base,altura)
        super().area(base,altura)
        super().perimetro()
    pass
