class Orden:
    contador_ordenes = 0

    @classmethod
    def _contador_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, computadoras):
        self._id_orden = Orden._contador_ordenes()
        self._computadoras = computadoras

    def agregar_computadoras(self, computadoras):
        self._computadoras.append(computadoras)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
            Orden: {self._id_orden}
            Computadora: {computadoras_str}
        '''
