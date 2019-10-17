import pickle


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def mostrar(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n")


coche1 = Vehiculo("Dacia", "Sandero")
coche2 = Vehiculo("Seat", "500")
coche3 = Vehiculo("Peugeot", "308")

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

# Ahorra rescatamos

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    c.mostrar()
