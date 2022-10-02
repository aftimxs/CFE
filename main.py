from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import sqlite3
import NEGOCIO
import const
import functions
import csv
import time
import wx
#import x


#class UI(x.Mywin):
#    def __init__(self, parent):
#        x.Mywin.__init__(self, parent)

def CFE():
    # Accesar al driver y actions
    PATH = "/Users/aftimxs/Downloads/chromedriver"
    #C:\Program Files(x86)\chromedriver.exe
    driver = webdriver.Chrome(PATH)
    actions = ActionChains(driver)

    S_servicio = input('Servicio: ').upper()
    S_tarifa = input('Tarifa: ').upper()
    S_anio = input('Año: ').upper()
    S_mes = input('Mes: ').upper()

    if S_mes == 'TODOS':
        pass
    else:
        S_mes = str(const.D_meses[S_mes])


    for key, val in const.funciones.items():
        if key == S_servicio:
            val(driver, actions, S_servicio, S_tarifa, S_anio, S_mes)
        else:
            pass


CFE()

#app = wx.App(False)
#frame = UI(None)
#frame.Show(True)
##start the applications
#app.MainLoop()