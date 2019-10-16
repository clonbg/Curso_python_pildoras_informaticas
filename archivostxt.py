from io import open

# Modo escritura
""" archivo_texto = open("archivo.txt", "w")

frase = "Contenido para el archivo de texto\nel miércoles"

archivo_texto.write(frase)

archivo_texto.close() """

# Modo lectura

""" archivo_texto = open("archivo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto) """

# Modo lectura linea a linea

""" archivo_texto = open("archivo.txt", "r")

lineas_texto = archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)
print(lineas_texto[1]) """

# Modo añadir contenido

""" archivo_texto = open("archivo.txt", "a")

archivo_texto.write("\nEsta es una nueva línea") """

# Posición del cursor

""" archivo_texto = open("archivo.txt", "r")

print(archivo_texto.read())

archivo_texto.seek(0)

print(archivo_texto.read())

archivo_texto.seek(23)

print(archivo_texto.read())

archivo_texto.seek(0)

print(archivo_texto.read(11))

print(archivo_texto.read()) """

# Lectura y escritura

archivo_texto = open("archivo.txt", "r+")

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Escrito desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.seek(0)

print(archivo_texto.read())

archivo_texto.close()
