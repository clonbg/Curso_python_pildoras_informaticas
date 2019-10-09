def divide(num1,num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "No se puede dividir por cero"

while True:
    try:
        num1=int(input("Primer número: "))
        num2=int(input("Segundo número: "))
        break
    except ValueError:
        print("Deben ser valores numéricos")

divide(num1,num2)
    
print("final")