from math import pi

class Figura:
    def __init__(self,base,altura,radio) :
        self.base = base
        self.altura = altura
        self.radio = radio
    
class Rectangulo(Figura):
    def __init__(self,base,altura) :
        Figura.__init__(self,base,altura)
        
    def area(self):
        area = self.base * self.altura
        print("Area :",area)

    def perimetro(self):
        periimetro = (self.base*2) + (self.altura*2)
        print("Perimetro :",periimetro)
    
class Circulo(Figura):
    def __init__(self,radio):
        Figura.__init__(self,radio)

    def area(self):
        area = (pi*self.radio)^2
        print("Area :",area)

    def perimetro(self):
        perimetro = (2*pi*self.radio)
        print('Perimetro :',perimetro)