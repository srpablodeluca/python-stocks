# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:54:18 2020

@author: Pablo
"""
import scrapy
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import os
import time

print(os.getcwd())

user = "sr.pablodeluca"
pwd = "Balanz1980"

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get("https://clientes.balanz.com/micuenta")
elem = driver.find_element_by_name("username")
elem.send_keys(user)
elem = driver.find_element_by_name("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

time.sleep(10)

pyautogui.moveTo(pyautogui.locateCenterOnScreen("Cotizaciones.png"), duration=1)

pyautogui.moveTo(pyautogui.locateCenterOnScreen("Acciones.png"), duration=1)

pyautogui.click(pyautogui.locateCenterOnScreen("Acciones.png"))


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://https://clientes.balanz.com/cotizaciones/acciones"  ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)







