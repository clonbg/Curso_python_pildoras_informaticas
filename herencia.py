class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def frenar(self):
        self.frena = True

    def mostrar(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enMarcha, "\nFrenando: ", self.frena)


class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Estoy haciendo el caballito"

    def mostrar(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enMarcha, "\nFrenando: ", self.frena, "\n", self.hcaballito)


miMoto = Moto("Honda", "CBR")
miMoto.mostrar()
miMoto.caballito()
miMoto.mostrar()


class VehiculoElectrico():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


# Coge el constructor de la clase del primer parámetro
class bicicletaElectrica(Vehiculo, VehiculoElectrico):
    pass


mibici = bicicletaElectrica("Orbea", "miniBici7680")

mibici.mostrar()
