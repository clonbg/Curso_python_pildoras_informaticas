miLista=["gato","perro","Marta","sombrero"]
print(miLista)
print(miLista[2])
print(miLista[-3])
print(miLista[1:3])

miLista.append("Lucas")
print(miLista)

miLista.insert(1, "Mis huevos")
print(miLista)

miLista.extend(["María","Mi amor"])
print(miLista)

print(miLista.index("Mi amor"))#Devuelve el primer resultado

print("gato" in miLista)

miLista.extend([3,6.25])
print(miLista)

miLista.remove("perro")
print(miLista)

miLista.pop()
print(miLista)

miLista2=["Federico", "Manuel"]
miLista+=miLista2
print(miLista)

miLista3=["Lluvia", "Sol"] * 3
print(miLista3)