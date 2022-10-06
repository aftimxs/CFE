from tkinter import *
from tkinter import ttk
import main

root = Tk()
root.title("Base de datos CFE")


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
    'ZACATECAS',
    'TODOS'
]


def pick_tarifa(e):
    if drop_s.get() == 'HOGAR':
        drop_t.config(values=tarifas_hogar)
    elif drop_s.get() == 'NEGOCIO':
        drop_t.config(values=tarifas_negocio)


def pick_zona(e):
    if drop_s.get() == 'NEGOCIO':
        drop_estado.pack()
        mun.pack()
        div.pack()
    else:
        pass


def submit():
    S_servicio = drop_s.get()
    S_anio = drop_a.get()
    S_mes = drop_m.get()
    S_tarifa = drop_t.get()

    S_estado = drop_estado.get()
    S_municipio = mun.get().upper()
    S_div = div.get().upper()

    main.CFE(S_servicio, S_anio, S_mes, S_tarifa, S_estado, S_municipio, S_div)


drop_s = ttk.Combobox(frame_Serv, values=servicios)
drop_s.current(0)
drop_s.pack()
drop_s.bind('<<ComboboxSelected>>', pick_tarifa)

drop_a = ttk.Combobox(frame_Year, values=years)
drop_a.current(0)
drop_a.pack()

drop_m = ttk.Combobox(frame_Month, values=meses)
drop_m.current(0)
drop_m.pack()

drop_t = ttk.Combobox(frame_tarifas, values=[' '])
drop_t.current(0)
drop_t.pack()
drop_t.bind('<<ComboboxSelected>>', pick_zona)

drop_estado = ttk.Combobox(frame_zona, values=estados)
drop_estado.current(0)

mun = Entry(frame_zona, width=30)
mun.insert(0, 'Municipio')

div = Entry(frame_zona, width=30)
div.insert(0, 'Division')


subbut = Button(root, text='Submit', padx=50, command=submit)
subbut.grid(row=3, column=0, columnspan=2, pady=15)


root.mainloop()