import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

#se declara la ubicacion del driver
PATH = '/usr/local/bin/chromedriver'

class Automatization(unittest.TestCase):

    #Inicio del test
    def setUp(self):
        
        #se llama al driver del navegagor
        self.driver = webdriver.Chrome(executable_path=PATH)
        driver = self.driver
        #da 30 seg de espera para que responda
        driver.implicitly_wait(30)
        #maximiza la pantalla
        driver.maximize_window()
        #ingresa a la direccion de internet deseada
        driver.get('https://www.rug.gob.mx/Rug/home/inicio.do?fbclid=IwAR3RBgy45BNhDv46lw-nK_ZhifuoJHlgHn8zJf9My4qgaL4G8WVmLEeJb28')


    def test_login(self):

        driver = self.driver
        #busca el boton de "ingresar"
        xpath_ingresa = '//*[@id="workingContainer"]/main/form/div[1]/div[2]/div[2]/div/input'
        ingresa = driver.find_element_by_xpath(xpath_ingresa)
        ingresa.click()

        #busca el cuadro de testo "usuario"
        usuario = driver.find_element_by_name('j_username')
        #busca el cuadro de texto "contraeña"
        contrasenia = driver.find_element_by_id('j_password')
        #busca el boton ingresar
        ingresa2 = driver.find_element_by_name('Ingresar')

        #corrobora que estan habilitadas las casillas y el boton
        self.assertTrue(usuario.is_enabled()
        and contrasenia.is_enabled()
        and ingresa2.is_enabled()
        )

        #ingresa el nombre del usuario
        usuario.send_keys('lhuertasg@inbursa.com')
        #ingresa la contraseña
        contrasenia.send_keys('GFI_MontSe_2005')
        #da click al boton
        ingresa2.click()

        #busca en el menu la opcion de "Inscripcion"
        inscripcion = driver.find_element_by_id('cuatroMenu')
        #corrobora que este habilitada
        self.assertTrue(inscripcion.is_enabled())
        #da click en la opcion "inscripcion"
        inscripcion.click()
        
        #busca la lista de opciones del acredor
        acredor = Select(driver.find_element_by_name('idAcreedorTO'))
        #selecciona al acredor "FC FINANCIAL SA DE CV SOFOM ER GRUPO FINANCIERO INBURSA"
        acredor.select_by_visible_text('FC FINANCIAL SA DE CV SOFOM ER GRUPO FINANCIERO INBURSA')

        #busca el boton de aceptar 
        aceptar = driver.find_element_by_id('baceptar')
        #da click en el boton de aceptar
        aceptar.click()

        #busca la lista de la de tipo de persona
        TipoPersona = Select(driver.find_element_by_id('tipoPersona'))
        #selecciona la opcion de "persona fisica"
        TipoPersona.select_by_visible_text('Persona Fisica')
        
        #busca la lista de nacionalidad
        Nacionalidad=Select(driver.find_element_by_id('nacionalidad'))
        #selecciona la opcion de Mexico
        Nacionalidad.select_by_visible_text('MÉXICO')

        time.sleep(10)

        
    #Salida de la prueba
    def tear_Down(self):
        self.driver.quit()

        


if __name__ == "__main__":
    unittest.main(verbosity=2)
