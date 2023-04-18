from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor


class Computadora:
    contador_computadoras = 0

    @classmethod
    def _contador_computadoras(cls):
        cls.contador_computadoras += 1
        return cls.contador_computadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._id_computadora = Computadora._contador_computadoras()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 15.6)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
