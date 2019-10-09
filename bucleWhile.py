import math

i = 1

while i <= 10:
    print(i, end=" ")
    i = i+1

edad = int(input("Introduce la edad: "))

while edad < 0 or edad > 100:
    print("Has introducido una edad incorrecta")
    edad = int(input("Introduce la edad: "))

print("Raiz cuadrada de 5 es : " + str(math.sqrt(5)))

# Video 17 ej 1
numero = int(input("Introduzca el número: "))
numero2 = int(input("Introduzca un número más alto que el anterior: "))
while numero < numero2:
    numero = numero2
    numero2 = int(input("Introduzca un número más alto que el anterior: "))
print(f"El {numero2} no es mayor que el {numero}")

# Video 17 ej 2
positivo = int(input("Introduce un número positivo: "))
suma = 0
while positivo > 0:
    suma = suma+positivo
    positivo = int(input("Introduce un número positivo: "))
print(f"{positivo} no es un número positivo, y la suma de todos es: {suma}")
