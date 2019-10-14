class Coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")


vehiculo1 = Moto()
vehiculo1.desplazamiento()

vehiculo2 = Coche()
vehiculo2.desplazamiento()

vehiculo3 = Camion()
vehiculo3.desplazamiento()


def desplazar(objeto):
    objeto.desplazamiento()


desplazar(vehiculo3)
