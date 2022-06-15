
class A:
    def __init__(self):
        print('SOY LA CLASE A')
    def a(self):
        print('SOY METODO DE A')

class B:
    def __init__(self):
        print('SOY LA CLASE B')
    def b(sef):
        print('SOY METODO DE B')
#LA HERENCIA MULTIPLE LE DA MAS IMPORTANNCIA AL QUE ESTA EN LA IZQUIERDA EN ESTA CASO LA CLASE A
class C(A,B):
    def c(self):
        print('SOY METODO DE C')

c1 = C()#devolvera el mensake de soy de la clase A por la importancia antes mencionada

class C(B,A):
    def c(self):
        print('soy meotod de la clase c')

c1 = C()#devolvera el nombre soy de la clase b, por la importantcia antes mecionada

c1.a() #devuelve soy de la clase a, por que se esta llamando el metodo 'a' heredado 
c1.b() #devuelve soy de la clase b. por que se esta llamando el metodo 'b' heredado
c1.c() #devuelve soy de la clase c, por que se esta llamando el metodo 'c' heredado