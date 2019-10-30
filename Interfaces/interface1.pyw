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

Label(miFrame, text="Esta es una etiqueta", bg="gray", fg="black", font=("Liberation Serif",15)).place(x=50,y=20)

miImagen=PhotoImage(file="pc.gif")

Label(miFrame, image=miImagen,bg="gray").place(x=60,y=50)

Entry(miFrame,bg="white").place(x=130,y=180)

Label(miFrame, text="Nombre: ", bg="gray").place(x=50,y=180)

raiz.mainloop()

