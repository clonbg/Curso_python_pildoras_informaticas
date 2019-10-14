email = input("Introduce una dirección de email válida: ")


def validar(texto):
    bool = True
    if (texto.count("@") != 1 or texto.startswith("@") or texto.endswith("@")):
        bool = False
    return bool


if (validar(email)):
    print("Válido")
else:
    print("No válido")
