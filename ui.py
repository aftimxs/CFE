from tkinter import *
from tkinter import ttk
import main

root = Tk()
root.title("Base de datos CFE")
#root.geometry('200x400')

frame_Serv = LabelFrame(root, text='SERVICIO', padx=15, pady=10)
frame_Serv.grid(row=0, column=0, padx=10, pady=10)

frame_Year = LabelFrame(root, text='AÑO', padx=17, pady=10)
frame_Year.grid(row=1, column=0, padx=10, pady=10)

frame_Month = LabelFrame(root, text='MES', padx=17, pady=10)
frame_Month.grid(row=1, column=1, padx=10, pady=10)

frame_tarifas = LabelFrame(root, text='TARIFA', padx=17, pady=10)
frame_tarifas.grid(row=0, column=1, padx=10, pady=10)

frame_zona = LabelFrame(root, text='ZONA', padx=17, pady=10)
frame_zona.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

servicios = [
    'HOGAR',
    'NEGOCIO',
    'INDUSTRIA',
    'TODOS'
]

years = [
    '2022',
    '2021',
    '2020',
    '2019',
    'TODOS'
]

meses = [
    'ENERO',
    'FEBRERO',
    'MARZO',
    'ABRIL',
    'MAYO',
    'JUNIO',
    'JULIO',
    'AGOSTO',
    'SEPTIEMBRE',
    'OCTUBRE',
    'NOVIEMBRE',
    'DICIEMBRE',
    'TODOS'
]

tarifas_hogar = [
    '1',
    '1A',
    '1B',
    '1C',
    '1D',
    '1E',
    '1F',
    'DAC',
    'TODAS'
]

tarifas_negocio = [
    'PDBT',
    'GDBT',
    'GDMTO',
    'GDMTH',
    'TODAS'
]

estados = [
    'AGUASCALIENTES',
    'BAJA CALIFORNIA',
    'BAJA CALIFORNIA SUR',
    'CAMPECHE',
    'CHIAPAS',
    'CHIHUAHUA',
    'CIUDAD DE MÉXICO',
    'COAHUILA',
    'COLIMA',
    'DURANGO',
    'ESTADO DE MÉXICO',
    'GUANAJUATO',
    'GUERRERO',
    'HIDALGO',
    'JALISCO',
    'MICHOACÁN',
    'MORELOS',
    'NAYARIT',
    'NUEVO LEÓN',
    'OAXACA',
    'PUEBLA',
    'QUERÉTARO',
    'QUINTANA ROO',
    'SAN LUIS POTOSÍ',
    'SINALOA',
    'SONORA',
    'TABASCO',
    'TAMAULIPAS',
    'TLAXCALA',
    'VERACRUZ',
    'YUCATÁN',
    'ZACATECAS'
]


def pick_tarifa(e):
    if S_servicio.get() == 'HOGAR':
        S_tarifa.config(values=tarifas_hogar)
    elif S_servicio.get() == 'NEGOCIO':
        S_tarifa.config(values=tarifas_negocio)

        drop_estado = ttk.Combobox(frame_zona, values=estados)
        drop_estado.current(0)
        drop_estado.pack()

        mun = Entry(frame_zona, width=30)
        mun.insert(0, 'Municipio')
        mun.pack()

        div = Entry(frame_zona, width=30)
        div.insert(0, 'Division')
        div.pack()
        return drop_estado, mun, div


def submit():
    S_servicio.get()
    S_anio.get()
    S_mes.get()
    S_tarifa.get()

    #drop_estado.get()
    #mun.get()
    #div.get()


S_servicio = ttk.Combobox(frame_Serv, values=servicios)
S_servicio.current(0)
S_servicio.pack()
S_servicio.bind('<<ComboboxSelected>>', pick_tarifa)

S_anio = ttk.Combobox(frame_Year, values=years)
S_anio.current(0)
S_anio.pack()

S_mes = ttk.Combobox(frame_Month, values=meses)
S_mes.current(0)
S_mes.pack()

S_tarifa = ttk.Combobox(frame_tarifas, values=[' '])
S_tarifa.current(0)
S_tarifa.pack()

subbut = Button(root, text='Submit', padx=50, command=submit).grid(row=3, column=0, columnspan=2, pady=15)


root.mainloop()