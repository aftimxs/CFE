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


def CFE(S_servicio, S_anio, S_mes, S_tarifa, S_estado, S_municipio, S_div):
    # Accesar al driver y actions
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    #
    #/Users/aftimxs/Downloads/chromedriver
    driver = webdriver.Chrome(PATH)
    actions = ActionChains(driver)

    if S_mes == 'TODOS':
        pass
    else:
        S_mes = str(const.D_meses[S_mes])

    if S_servicio == 'HOGAR':
        HOGAR.HOGAR(driver, actions, S_tarifa, S_anio, S_mes)
    else:
        NEGOCIO.NEGOCIO(driver, actions, S_tarifa, S_anio, S_mes, S_estado, S_municipio, S_div)

