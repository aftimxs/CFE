from tkinter import *

root = Tk()
root.title("Base de datos CFE")
root.geometry('200x200')

HOGAR = IntVar()
NEGOCIO = IntVar()
INDUSTRIA = IntVar()

label1 = Label(root, text='SERVICIO').pack()
s1 = Checkbutton(root, text = 'Hogar', variable= HOGAR).pack()
s2 = Checkbutton(root, text = 'Negocio', variable= NEGOCIO).pack()
s3 = Checkbutton(root, text = 'Industria', variable= INDUSTRIA).pack()

root.mainloop()