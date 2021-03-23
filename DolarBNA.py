from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from selenium import webdriver as web

url = 'https://www.errepar.com/cotizacion-dolar'

# Selectores:
boton_ultimoMes = '#aspnetForm > div:nth-child(4) > div > div.col-sm-8.col-sm-push-4.col-md-push-4.contentdiv > section > div:nth-child(5) > div:nth-child(3) > p > a'
selector_tabla = '#ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder2_updPnl > div:nth-child(3)'

driver = web.Chrome()
driver.maximize_window()
driver.get(url)
driver.find_element_by_css_selector(boton_ultimoMes).click()

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Tabla

td = soup.find_all('td', class_='lateral2')

# print(td)

tabla = list()
count = 0
for a in td:
    if count < 5:
        tabla.append(a.text)
    else:
        break
    count += 1

encabezados = ['Fecha', 'Billete Compra', 'Billete Venta', 'Divisa Compra', 'Divisa Venta']

print(tabla)

df = pd.DataFrame({'Titulos': encabezados, 'Datos': tabla})

diccionario = dict(zip(encabezados, tabla))

print(diccionario)

probando = pd.DataFrame([diccionario])

print(probando)
probando.to_excel('Cotizaciones.xlsx', index=False)
