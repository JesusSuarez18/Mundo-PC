class Monitor:
    contador_monitor = 0

    @classmethod
    def _contador_monitor(cls):
        cls.contador_monitor += 1
        return cls.contador_monitor

    def __init__(self, marca, tamanio):
        self._id_monitor = Monitor._contador_monitor()
        self._marca = marca
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self):
        return f'ID: {self._id_monitor} Marca: {self._marca} Tamaño: {str(self._tamanio)}'


if __name__ == '__main__':
    monitor1 = Monitor('HP', 15.6)
    monitor2 = Monitor('DELL', 17.5)
    print(monitor1)
    print(monitor2)
