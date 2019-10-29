from tkinter import *

raiz=Tk()

raiz.resizable(0,0)

raiz.iconbitmap('@/home/clonbg/Git/Curso_python_pildoras_informaticas/Interfaces/moon.xbm')

raiz.title("Primera ventana")

#raiz.geometry("600x400") se redimensiona con el tamaño del frame

raiz.config(bg="gray")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="600", height="400")

miFrame.config(bd="20")

miFrame.config(relief="flat")

raiz.mainloop()