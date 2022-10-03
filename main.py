from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import const
import NEGOCIO
import HOGAR

import csv
import time
import wx
#import x


#class UI(x.Mywin):
#    def __init__(self, parent):
#        x.Mywin.__init__(self, parent)

def CFE(S_servicio, S_anio, S_mes, S_tarifa):
    # Accesar al driver y actions
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    #/Users/aftimxs/Downloads/chromedriver
    driver = webdriver.Chrome(PATH)
    actions = ActionChains(driver)

    #S_servicio = input('Servicio: ').upper()
    #S_tarifa = input('Tarifa: ').upper()
    #S_anio = input('Año: ').upper()
    #S_mes = input('Mes: ').upper()
#
    #if S_servicio == 'NEGOCIO':
    #    S_estado = input('Estado: ').upper()
    #    S_municipio = input('Municipio: ').upper()
    #    S_div = input('Division: ').upper()
#
    #else:
    #    pass

    if S_mes == 'TODOS':
        pass
    else:
        S_mes = str(const.D_meses[S_mes])

    if S_servicio == 'HOGAR':
        HOGAR.HOGAR(driver, actions, S_tarifa, S_anio, S_mes)
    else:
        NEGOCIO.NEGOCIO(driver, actions, S_tarifa, S_anio, S_mes)
#, S_estado, S_municipio, S_div


#app = wx.App(False)
#frame = UI(None)
#frame.Show(True)
##start the applications
#app.MainLoop()