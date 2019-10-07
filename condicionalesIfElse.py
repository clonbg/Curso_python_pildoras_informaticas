# If
print("Notas de alumnos")

notaAlumno = int(input("Introduzca la nota: "))


def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


print(evaluacion(5))
print(evaluacion(4))
print(evaluacion(notaAlumno))

# If else
print("Verificación de acceso")

edadUsuario = int(input("Introduzca la edad: "))

if edadUsuario < 18:
    print("No puedes pasar")
elif edadUsuario > 130:
    print("Estarías muerto")
else:
    print("Puedes pasar")

# número mas alto con funcion DevuelveMax
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))


def devuelveMax(num1, num2):
    if num1 > num2:
        print("El " + str(num1) + " es el número mayor")
    elif num2 > num1:
        print("El " + str(num2) + " es el número mayor")
    else:
        print("Los números son iguales")


devuelveMax(num1, num2)

# Nombre, dirección y teléfono en una lista
nombre = input("Escriba el nombre: ")
direccion = input("Escriba la dirección: ")
telefono = input("Escriba el teléfono: ")

miLista = [nombre, direccion, telefono]

print("Los datos personales son: "
      + miLista[0] + ", " + miLista[1] + ", " + miLista[2])

# Media arítmetica de 3 números
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

print("La media aritmética de los tres números es: " + str((num1+num2+num3)/3))

# Concatenación lógicos
edad = 71

if 0 < edad < 100:
    print("Edad correcta")

bares = 0
parques = 1

if edad >= 18 and bares > 0 or parques > 0:
    print("Oleeeeeee")

alimento = input("Introduce un alimento: ")

alimento = alimento.lower()

# alimento=alimento.upper()

if alimento in ("huevos", "leche"):
    print("Está en la lista")
