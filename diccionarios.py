miDiccionario={
	"nombre": "Manuel",
	"dni": 22222222
}
print(miDiccionario)
print(miDiccionario["nombre"])

miDiccionario["telefono"]="690690690"
print(miDiccionario)

del miDiccionario["dni"]
print(miDiccionario)

miDiccionario2={
	23:"Jordan",
	"Nombre":"Michael",
	"Equipo":"Chicago",
	"anillos":[1991,1992,1993,1996,1997,1998]
}
print(miDiccionario2["anillos"])

miDiccionario2={
	23:"Jordan",
	"Nombre":"Michael",
	"Equipo":"Chicago",
	"anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}
}
print(miDiccionario2["anillos"])
print(miDiccionario2.keys())
print(miDiccionario2.values())
print(len(miDiccionario2))
print(len(miDiccionario2["anillos"]))
print(len(miDiccionario2["anillos"]["temporadas"]))