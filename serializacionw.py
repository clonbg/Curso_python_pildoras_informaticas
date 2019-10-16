import pickle

lista_nombres = ["Manuel", "María", "Luisa", "Fede"]

# Escritura binaria
fichero_binario = open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)
