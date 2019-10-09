def divide():
    try:
        num1=float(input("Primer número: "))
        num2=float(input("Segundo número: "))
        print(f"El resultado es {num1/num2}")
    except ValueError:
        print("No son números")
    except ZeroDivisionError:
        print("No se puede dividir entre o")
    finally:
        print("Finalizado")

divide()

def divide2():
    try:
        num1=float(input("Primer número: "))
        num2=float(input("Segundo número: "))
        print(f"El resultado es {num1/num2}")
    except:
        print("Error")

divide2()