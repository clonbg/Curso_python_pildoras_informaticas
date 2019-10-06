#No se pueden modificar
tupla1=("sombrero", "gorra", "boina")
print(tupla1)
#se imprime con paréntesis

miLista=list(tupla1)
print(miLista)
#Se imprime con corchetes

tupla2=tuple(miLista)
print(tupla2)

print(tupla1.count("gorra"))

print(len(tupla2))

#tupla con 1 elemento
tuplaUnitaria=("Pedro",)
print(tuplaUnitaria)

tupla3="hty","kjhkj",78
print(tupla3)

tupla4="Manuel",27,6,1975
nombre, dia, mes, año=tupla4
print(tupla4[0])
print(tupla4[1])
print(tupla4[2])
print(tupla4[3])

print(tupla4.index(6))