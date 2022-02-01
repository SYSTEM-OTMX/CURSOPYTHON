#PRIMERO EN ENTRAR , PRIMERO EN SALIR

from collections import deque#ayuda a elimar datos de un lista

cola = deque(['EDUARDO','EFRAIN','SANTOS'])

print(cola)

cola.append('ARELLANO')

print(cola)

cola.popleft()#eliminar elemento de la izquierda, simulando el primero en entrar

print(cola)

