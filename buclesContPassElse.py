for i in "Manuel":
    if i == "e":
        continue
    print(f"Viendo la letra {i}")

nombre = "funcion longitud"
letras = 0
for i in nombre:
    if i == " ":
        continue
    letras += 1
print(f"tiene {letras} letras")


def funcionImaginaria():
    pass  # para implementar luego


email = input("Introduce un email: ")
for i in email:
    if i == "@":
        arroba = True
        break
else:  # este else pertenece al for
    arroba = False

print(arroba)
