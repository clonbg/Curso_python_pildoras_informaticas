class Coche():
    largoChasis=250
    anchoChasis=150
    ruedas=4
    enMarcha=False

    def arrancar(self):
        self.enMarcha=True

    def mostrar(self):
        print("El largo es: "+str(self.largoChasis))
        print("El ancho es: "+str(self.anchoChasis))
        print("Tiene "+str(self.ruedas)+" ruedas")
        if self.enMarcha:
            print("Está en marcha")
        else:
            print("Está parado")

miCoche=Coche()

miCoche.mostrar()
miCoche.arrancar()
miCoche.mostrar()
