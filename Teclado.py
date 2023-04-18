from DispositivosEntrada import DispositivosEntrada


class Teclado(DispositivosEntrada):
    contador_teclado = 0

    @classmethod
    def _contador_teclado(cls):
        cls.contador_teclado += 1
        return cls.contador_teclado

    def __init__(self, marca, tipo_entrada):
        self._id_teclado = Teclado._contador_teclado()
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_teclado} {super().__str__()}'


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    teclado2 = Teclado('DELL', 'Bluetooth')
    print(teclado1)
    print(teclado2)
