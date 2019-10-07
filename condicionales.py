#If
print("Notas de alumnos")

notaAlumno=int(input("Introduzca la nota: "))

def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(5))
print(evaluacion(4))
print(evaluacion(notaAlumno))