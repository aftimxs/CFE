from tkinter import *

root = Tk()
root.title("Base de datos CFE")
root.geometry('200x400')

HOGAR = IntVar()
NEGOCIO = IntVar()
INDUSTRIA = IntVar()

enero = IntVar()
febrero = IntVar()
marzo = IntVar()
abril = IntVar()
mayo = IntVar()
junio = IntVar()
julio = IntVar()
agosto = IntVar()
septiembre = IntVar()
octubre = IntVar()
noviembre = IntVar()
diciembre = IntVar()

aa1 = IntVar()
aa2 = IntVar()
aa3 = IntVar()
aa4 = IntVar()

T1 = IntVar()
T1A = IntVar()
T1B = IntVar()
T1C = IntVar()
T1D = IntVar()
T1E = IntVar()
T1F = IntVar()
TDAC = IntVar()

def tarifas_hogar():
    th1 = Checkbutton(root, text='1', variable=T1).pack()
    th2 = Checkbutton(root, text='1A', variable=T1A).pack()
    th3 = Checkbutton(root, text='1B', variable=T1B).pack()
    th4 = Checkbutton(root, text='1C', variable=T1C).pack()
    th5 = Checkbutton(root, text='1D', variable=T1D).pack()
    th6 = Checkbutton(root, text='1E', variable=T1E).pack()
    th7 = Checkbutton(root, text='1F', variable=T1F).pack()
    th8 = Checkbutton(root, text='DAC', variable=TDAC).pack()

label1 = Label(root, text='SERVICIO').pack()
s1 = Checkbutton(root, text = 'Hogar', variable= HOGAR, command=tarifas_hogar).pack()
s2 = Checkbutton(root, text = 'Negocio', variable= NEGOCIO).pack()
s3 = Checkbutton(root, text = 'Industria', variable= INDUSTRIA).pack()

a1 = Checkbutton(root, text='2022', variable=aa1).pack()
a2 = Checkbutton(root, text='2021', variable=aa2).pack()
a3 = Checkbutton(root, text='2020', variable=aa3).pack()
a4 = Checkbutton(root, text='2019', variable=aa4).pack()

m1 = Checkbutton(root, text='Enero', variable=enero).pack()
m2 = Checkbutton(root, text='Febrero', variable=febrero).pack()
m3 = Checkbutton(root, text='Marzo', variable=marzo).pack()
m4 = Checkbutton(root, text='Abril', variable=abril).pack()
m5 = Checkbutton(root, text='Mayo', variable=mayo).pack()
m6 = Checkbutton(root, text='Junio', variable=junio).pack()
m7 = Checkbutton(root, text='Julio', variable=julio).pack()
m8 = Checkbutton(root, text='Agosto', variable=agosto).pack()
m9 = Checkbutton(root, text='Septiembre', variable=septiembre).pack()
m10 = Checkbutton(root, text='Octubre', variable=octubre).pack()
m11 = Checkbutton(root, text='Noviembre', variable=noviembre).pack()
m12 = Checkbutton(root, text='Diciembre', variable=diciembre).pack()




root.mainloop()