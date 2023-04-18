from Teclado import Teclado
from Raton import  Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import  Orden


teclado1 = Teclado('HP','USB')
raton1 = Raton('HP','USB')
monitor1 = Monitor('HP',15.6)
computadora1 = Computadora('HP',monitor1,teclado1,raton1)

teclado2 = Teclado('Acer','Inalambrico')
raton2 = Raton('Acer','Inalambrico')
monitor2 = Monitor('Acer',17.5)
computadora2 = Computadora('Acer',monitor2,teclado2,raton2)

computadoras1 = [computadora1,computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('DELL','USB')
raton3 = Raton('DELL','USB')
monitor3 = Monitor('DELL',16.8)
computadora3 = Computadora('DELL',monitor3,teclado3,raton3)

orden1.agregar_computadoras(computadora3)
print(orden1)