class Coche():
    def __init__(self):  # Constructor
        self.__largoChasis = 250
        self.__anchoChasis = 150  # __ encapsula
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self):
        if self.__enMarcha == False:
            comprobar = self.__chequeo()
        if comprobar:
            print("Está ok")
            self.__enMarcha = True
        else:
            print("No está ok")

    def mostrar(self):
        print("El largo es: "+str(self.__largoChasis))
        print("El ancho es: "+str(self.__anchoChasis))
        print("Tiene "+str(self.__ruedas)+" ruedas")
        if self.__enMarcha:
            print("Está en marcha")
        else:
            print("Está parado")

    def __chequeo(self):  # Encapsulado para que no se pueda llamar desde fuera de la clase
        puertas = "ok"  # pero sí desde la función arrancar
        aceite = "ok"
        gasolina = "ok"
        if puertas == "ok" and aceite == "ok" and gasolina == "ok":
            return True
        else:
            return False


miCoche = Coche()

miCoche.mostrar()
miCoche.arrancar()
miCoche.mostrar()

miCoche2 = Coche()

miCoche2.mostrar()
