import math

def evaluaEdad(edad):
    if edad<0:
        raise ErrorEdad("No puedes ser más joven de 0")
    elif edad<20:
        print("Joven")

evaluaEdad(4)
#evaluaEdad(-15)

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("No puede ser negativo")
    else:
        return math.sqrt(num1)

print(calculaRaiz(144))
print(calculaRaiz(184))
try:
    print(calculaRaiz(-144))
except ValueError as ErrorNegativo:
    print(ErrorNegativo)