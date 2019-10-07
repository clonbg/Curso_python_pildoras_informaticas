for i in [1, 2, 3, 4, 4, 4]:
    print(i, end=" ")

email = False
for i in "clonbg@feg.kil":
    if i == "@":
        email = True

if email:
    print("Es un correo")
else:
    print("No es un correo")

for i in range(78):
    print(i, end=" ")
