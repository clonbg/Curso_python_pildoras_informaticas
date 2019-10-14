nombre = input("Introduzca el nombre: ")
nombre = nombre.upper()
nombre = nombre.lower()
nombre = nombre.capitalize()
print("El nombre es: ", nombre)

edad = input("Introduce una edad: ")

while edad.isdigit() == False:
    edad = input("Introduce una edad: ")

if (int(edad) < 18):
    print("Menor")
else:
    print("Mayor")
