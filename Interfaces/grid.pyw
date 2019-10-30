from tkinter import *

raiz=Tk()

raiz.resizable(0,0)

raiz.iconbitmap('@/home/clonbg/Git/Curso_python_pildoras_informaticas/Interfaces/moon.xbm')

raiz.title("Primera ventana")

#raiz.geometry("600x400") se redimensiona con el tamaño del frame

raiz.config(bg="gray")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="gray")

miFrame.config(width="600", height="400")

miFrame.config(bd="20")

miFrame.config(relief="flat")

Label(miFrame, text="Esta es una etiqueta", bg="gray", fg="black", font=("Liberation Serif",15)).grid(row=0,column=0,columnspan=2)

miImagen=PhotoImage(file="pc.gif")

Label(miFrame, image=miImagen,bg="gray").grid(row=1,column=0,columnspan=2)

Entry(miFrame,bg="white").grid(row=2,column=1,pady=3,sticky="w")

Label(miFrame, text="Nombre: ", bg="gray").grid(row=2,column=0,sticky="w",pady=3)

Entry(miFrame,bg="white",width=40).grid(row=3,column=1,pady=3,sticky="w")

Label(miFrame, text="Apellidos: ", bg="gray").grid(row=3,column=0,sticky="w",pady=3)

Entry(miFrame,bg="white",width=40).grid(row=4,column=1,pady=3,sticky="w")

Label(miFrame, text="Dirección: ", bg="gray").grid(row=4,column=0,sticky="w",pady=3)

Entry(miFrame,bg="white",width=40,show="*").grid(row=5,column=1,pady=3,sticky="w")

Label(miFrame, text="Password: ", bg="gray").grid(row=5,column=0,sticky="w",pady=3)

raiz.mainloop()

