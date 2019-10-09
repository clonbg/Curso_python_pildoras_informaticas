def funcionPares(limite):
    num = 2
    listaPares = []
    while num < limite:
        listaPares.append(num)
        num = num+2
    return listaPares


print(funcionPares(16))


def generarPares(limite):
    num = 2
    while num < limite:
        yield num
        num = num+2


devuelvePares = generarPares(16)

''' for i in devuelvePares:
    print(i) '''

print(next(devuelvePares))

print("Más código")

print(next(devuelvePares))

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        ''' for subElemento in elemento:
            yield subElemento '''
        yield from elemento

ciudades=devuelve_ciudades("Madrid", "Valencia", "Bilbao", "Sevilla", "Barcelona")

print(next(ciudades))