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
import const
import csv
import time


def NEGOCIO(driver, actions, S_tarifa, S_anio, S_mes, S_estado, S_municipio, S_div):
    driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Negocio.aspx')

    conn = sqlite3.connect('NEGOCIO.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE TNG(tarifa, estado, municipio, division, anio, mes, cargo, unidades, costo)")

    opciones_tarifas = driver.find_elements(By.XPATH, "//div[@id='ContentPlaceHolder1_pnlTarifasCRE']/div[2]/p/a")

    templist = []

    if S_tarifa == 'TODAS':
        for index, val in enumerate(opciones_tarifas):
            try:
                opciones_tarifas = driver.find_elements(By.XPATH, "//div[@id='ContentPlaceHolder1_pnlTarifasCRE']/div[2]/p/a")
                actions.move_to_element(opciones_tarifas[index]).perform()
                opciones_tarifas[index].click()
                cuales_anios(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div)

                driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Negocio.aspx')
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@id='ContentPlaceHolder1_pnlTarifasCRE']/div[2]/p/a")))
            except StaleElementReferenceException:
                pass
        conn.close()
    else:
        try:
            opciones_tarifas = driver.find_element(By.PARTIAL_LINK_TEXT, S_tarifa)
            actions.move_to_element(opciones_tarifas).perform()
            opciones_tarifas.click()
            cuales_anios(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div)

            driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Negocio.aspx')
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='ContentPlaceHolder1_pnlTarifasCRE']/div[2]/p/a")))
        except StaleElementReferenceException:
            pass
        conn.close()


def cuales_anios(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div):
    titulo = 'tituloContenidoRojo'

    #Obtener nombre de la tarifa y minimo mensual de consumo
    nombre_tarifa = driver.find_element(By.CLASS_NAME, titulo).text.replace('Tarifa', '')

    #Opciones de años
    select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))

    #Loop por cada una de las opciones de año
    if S_anio == 'TODOS':
        for h in range(0, 3):
            #len(select_year.options)
            #Seleccionar año
            select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
            select_year.select_by_index(h)

            #Obtener nombre del año
            select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
            a = select_year.first_selected_option.text
            Estado(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, nombre_tarifa)
    else:
        # Seleccionar año
        select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
        select_year.select_by_value(S_anio)

        # Obtener nombre del año
        select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
        a = select_year.first_selected_option.text
        Estado(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, nombre_tarifa)


def Estado(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, nombre_tarifa):
    id_estado = 'ContentPlaceHolder1_EdoMpoDiv_ddEstado'
    if S_estado == 'TODOS':
        # Opciones de meses
        select_estado = Select(driver.find_element(By.ID, id_estado))
        # Loop por cada una de las opciones de estados
        for i in range(1, len(select_estado.options)):
            # Seleccionar estado
            select_estado = Select(driver.find_element(By.ID, id_estado))
            select_estado.select_by_value(f'{i}')

            # Obtener nombre del mes
            select_estado = Select(driver.find_element(By.ID, id_estado))
            e = select_estado.first_selected_option.text
            Municipio(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, nombre_tarifa)

    else:
        select_estado = Select(driver.find_element(By.ID, id_estado))
        select_estado.select_by_visible_text(S_estado)

        # Obtener nombre del mes
        select_estado = Select(driver.find_element(By.ID, id_estado))
        e = select_estado.first_selected_option.text
        Municipio(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, nombre_tarifa)


def Municipio(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, nombre_tarifa):
    id_municipio = 'ContentPlaceHolder1_EdoMpoDiv_ddMunicipio'
    if S_municipio == 'TODOS':
        # Opciones de meses
        select_municipio = Select(driver.find_element(By.ID, id_municipio))
        # Loop por cada una de las opciones de estados
        for i in range(1, len(select_municipio.options)):
            # Seleccionar estado
            select_municipio = Select(driver.find_element(By.ID, id_municipio))
            select_municipio.select_by_value(f'{i}')

            # Obtener nombre del mes
            select_municipio = Select(driver.find_element(By.ID, id_municipio))
            mun = select_municipio.first_selected_option.text
            Division(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, mun, nombre_tarifa)

    else:
        select_municipio = Select(driver.find_element(By.ID, id_municipio))
        select_municipio.select_by_visible_text(S_municipio)

        # Obtener nombre del mes
        select_municipio = Select(driver.find_element(By.ID, id_municipio))
        mun = select_municipio.first_selected_option.text
        Division(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, mun, nombre_tarifa)

def Division(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, mun, nombre_tarifa):
    id_div = 'ContentPlaceHolder1_EdoMpoDiv_ddDivision'
    if S_div == 'TODOS':
        # Opciones de meses
        select_div = Select(driver.find_element(By.ID, id_div))
        # Loop por cada una de las opciones de estados
        for i in range(1, len(select_div.options)):
            # Seleccionar estado
            select_div = Select(driver.find_element(By.ID, id_div))
            select_div.select_by_value(f'{i}')

            # Obtener nombre del mes
            select_div = Select(driver.find_element(By.ID, id_div))
            d = select_div.first_selected_option.text
            cuales_meses(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, mun, d, nombre_tarifa)

    else:
        select_div = Select(driver.find_element(By.ID, id_div))
        select_div.select_by_visible_text(S_div)

        # Obtener nombre del mes
        select_div = Select(driver.find_element(By.ID, id_div))
        d = select_div.first_selected_option.text
        cuales_meses(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, mun, d, nombre_tarifa)


def cuales_meses(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, e, mun, d, nombre_tarifa):
    id_mes = 'ContentPlaceHolder1_Fecha2_ddMes'
    if S_mes == 'TODOS':
        # Opciones de meses
        select_month = Select(driver.find_element(By.ID, id_mes))
        # Loop por cada una de las opciones de meses
        for i in range(1, len(select_month.options)):
            # Seleccionar mes
            select_month = Select(driver.find_element(By.ID, id_mes))
            select_month.select_by_value(f'{i}')

            # Obtener nombre del mes
            select_month = Select(driver.find_element(By.ID, id_mes))
            m = select_month.first_selected_option.text
            tabla(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, m, e, mun, d, nombre_tarifa)

    else:
        select_month = Select(driver.find_element(By.ID, id_mes))
        select_month.select_by_value(S_mes)

        # Obtener nombre del mes
        select_month = Select(driver.find_element(By.ID, id_mes))
        m = select_month.first_selected_option.text
        tabla(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, m, e, mun, d, nombre_tarifa)


def tabla(driver, templist, S_anio, S_mes, cur, conn, S_estado, S_municipio, S_div, a, m, e, mun, d, nombre_tarifa):
    table = driver.find_element(By.CSS_SELECTOR, '.table.table-bordered.table-striped')
    #Obtener las secciones que tienen los consumos
    rangos = table.find_elements(By.TAG_NAME, 'tr')

    for rango in rangos[1:]:
        #Extraer tipo de consumo, precio y limite de kwh
        x = rango.find_elements(By.TAG_NAME, 'td')
        tl = []

        for y in x:
            #Separar tipo de consumo, precio y limite de kwh, y mandarlos a una lista, quitar los espacios y acentos
            tl.append(y.text.replace('á', 'a').replace(' ', ''))

        #Hacer una entrada de diccionario con toda la info
        Table_dict = {
            'Tarifa': nombre_tarifa,
            'Estado': e,
            'Municipio': mun,
            'Division': d,
            'Anio': a,
            'Mes': m,
            'Cargo': tl[0],
            'Unidades': tl[1],
            'Costo': tl[2]
        }
        data = [nombre_tarifa, e, mun, d, a, m, tl[0], tl[1], tl[2]]
        #Mandar la entrada a una lista externa
        templist.append(Table_dict)
        cur.executemany("INSERT INTO TNG VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [data])
        conn.commit()

    #Hacer el file con la info
    df = pd.DataFrame(templist)
    df.to_csv(f'{nombre_tarifa}.csv')

