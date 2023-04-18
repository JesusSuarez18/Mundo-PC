from DispositivosEntrada import DispositivosEntrada


class Raton(DispositivosEntrada):
    contador_raton = 0

    @classmethod
    def _contador_raton(cls):
        cls.contador_raton += 1
        return cls.contador_raton

    def __init__(self, marca, tipo_entrada):
        self._id_raton = Raton._contador_raton()
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_raton} {super().__str__()}'


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('DELL', 'Inalambrico')
    print(raton2)
