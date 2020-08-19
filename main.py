import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import os


PATH = '/usr/local/bin/chromedriver'

class Automatization(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=PATH)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.rug.gob.mx/Rug/home/inicio.do?fbclid=IwAR3RBgy45BNhDv46lw-nK_ZhifuoJHlgHn8zJf9My4qgaL4G8WVmLEeJb28')


    def test_login(self):

        driver = self.driver

        xpath_ingresa = '//*[@id="workingContainer"]/main/form/div[1]/div[2]/div[2]/div/input'

        ingresa = driver.find_element_by_xpath(xpath_ingresa)
        #self.assertTrue(ingresa.is_enabled())
        ingresa.click()

        usuario = driver.find_element_by_name('j_username')
        contrasenia = driver.find_element_by_id('j_password')
        ingresa2 = driver.find_element_by_name('Ingresar')

        self.assertTrue(usuario.is_enabled()
        and contrasenia.is_enabled()
        and ingresa2.is_enabled()
        )

        usuario.send_keys('lhuertasg@inbursa.com')
        contrasenia.send_keys('GFI_MontSe_2005')
        ingresa2.click()

        inscripcion = driver.find_element_by_id('cuatroMenu')
        self.assertTrue(inscripcion.is_enabled())
        inscripcion.click()
        
        
    

    #Salida de la prueba
    def tear_Down(self):
        self.driver.quit()

        


if __name__ == "__main__":
    unittest.main(verbosity=2)
