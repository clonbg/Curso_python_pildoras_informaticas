import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Persona nueva: ", nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:

    personas = []

    def __init__(self):
        lista = open("ficheroPersonas", "ab+")
        lista.seek(0)
        try:
            self.personas = pickle.load(lista)
            print("Se cargaron {} personas del fichero externo".format(
                len(self.personas)))
        except:
            print("El fichero está vacio")
        finally:
            lista.close()
            del(lista)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasFichero()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasFichero(self):
        lista = open("ficheroPersonas", "wb")
        pickle.dump(self.personas, lista)
        lista.close()
        del(lista)

    def mostrarFichero(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista = ListaPersonas()
persona1 = Persona("Pedro", "Hombre", 34)
# persona2 = Persona("Marta", "Mujer", 56)

miLista.agregarPersonas(persona1)
# miLista.agregarPersonas(persona2)
# miLista.mostrarPersonas()

miLista.mostrarFichero()
