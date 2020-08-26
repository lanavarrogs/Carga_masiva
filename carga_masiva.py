import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import data
import archivo
import variables as var

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


    def login(self):
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
        usuario.send_keys(var.CORREO)
        #ingresa la contraseña
        contrasenia.send_keys(var.CONTRASENIA)
        #da click al boton
        ingresa2.click()
    

    def test_cicle(self):
        self.login()
        i = 0
        count = data.data_length()
        """while (i < count):
            self.page1(1)
            i += 1"""
        self.page1(2)

    def page1(self,id):
            driver = self.driver    
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

            self.condition(id)

            time.sleep(1)
            continuar = driver.find_element_by_id('buttonID')
            continuar.click()
                    
            self.page2(id)
                
    def condition(self,id):
        driver = self.driver
        #Variables del datasets
        fullname =  data.get_name(id)
        name = fullname[-1]
        apellidoPaterno = fullname[0]
        apellidoMaterno = fullname[1]
        electronic_folio = data.read_electronic_folio(id)
        RFC = data.read_RFC(id)
        Curp = data.read_CURP(id)
            
        #Cuando NO existe el folio electronico
        if electronic_folio == '':
            nombre =   driver.find_element_by_id('nombre')
            nombre.send_keys(name)

            Paterno = driver.find_element_by_id('apellidoPaterno')
            Paterno.send_keys(apellidoPaterno)

            Materno = driver.find_element_by_id('apellidoMaterno')
            Materno.send_keys(apellidoMaterno)
            
            if RFC == 'XAXX010101000':
                NoRFC = driver.find_element_by_id('rfcValidar1')
                NoRFC.click()
            else:
                rfc = driver.find_element_by_id('rfc')
                rfc.send_keys(RFC)
            
            CURP = driver.find_element_by_id('docExtranjero')
            CURP.send_keys(Curp)

            
            AceptarDatos = driver.find_element_by_xpath('//*[@id="botonGuardar"]/input')
            AceptarDatos.click()
            time.sleep(10)
            AceptarValores = driver.find_element_by_xpath('//*[@id="messageAlertDiv"]/div[2]/div[2]/input[1]')
            AceptarValores.click()

            NuevoFolio = driver.find_element_by_xpath('').text


            time.sleep(10)
            time.sleep(100)
            continuar = driver.find_element_by_xpath('//*[@id="buttonID"]')
            continuar.click()
            
            
        #en caso de que exista el folio electrinico
        else:
            
            NoFolio = driver.find_element_by_id('optotorgante')
            NoFolio.click()

            FolioEx = driver.find_element_by_id('folioExistente')
            FolioEx.send_keys(electronic_folio)

            ValidarFolio = driver.find_element_by_xpath('//*[@id="buttonValidar"]/input')
            ValidarFolio.click()
            
            #comprueba que si no tiene RFC
            if RFC == 'XAXX010101000':
                NoRFC = driver.find_element_by_id('rfcValidar1')
                NoRFC.click()
            
            #cuando si tienen RFC
            else: 
                print(RFC)   
                rfc = driver.find_element_by_xpath('//*[@id="rfcOtFolMoral"]')
                rfc.clear()
                rfc.send_keys(RFC)
                
                AcepRFC = driver.find_element_by_id('butonIDAceptar')
                AcepRFC.click()            

    def page2(self,id):

        driver = self.driver 

        Fecha_inicio = data.get_fecha_inicio(id)
        Monto_Inicial = str(data.get_monto_credito(id))
        Serie = data.get_no_serie(id)
        Fecha_fin = data.get_fecha_fin(id)

        TipoGarantia = Select(driver.find_element_by_id('idTipoGarantia'))
        TipoGarantia.select_by_visible_text('Prenda sin Transmisión de Posesión')
        
        FechaIni = driver.find_element_by_name('actoContratoTO.fechaCelebracion')
        FechaIni.send_keys(Fecha_inicio)

        mon_ini = driver.find_element_by_id('idMontoMaximo')
        mon_ini.send_keys(Monto_Inicial)

        TipoBien = Select(driver.find_element_by_id('formS2ag_actoContratoTO_tipoBienes'))
        TipoBien.select_by_visible_text('Vehículos de motor')

        descripcion = driver.find_element_by_name('actoContratoTO.descripcion')
        descripcion.send_keys(Serie)

        Bajo_protesta = driver.find_element_by_id('formS2ag_actoContratoTO_noGarantiaPreviaOt')
        Bajo_protesta.click

        Terminos = driver.find_element_by_id('formS2ag_actoContratoTO_otrosTerminos')
        Terminos.send_keys(archivo.terminos_condiciones)
        
        Acta_Contrato = driver.find_element_by_id('cpContrato')
        Acta_Contrato.click()

        FechaTer = driver.find_element_by_id('datepicker5')
        FechaTer.send_keys(Fecha_fin)

        ContinuarPag2 = driver.find_element_by_id('baceptar')
        ContinuarPag2.click()

        self.page3(id)


    
    def page3(self,id):
        driver = self.driver
        mes = str(data.get_month(id))

        meses = driver.find_element_by_id('formAcVig_inscripcionTO_meses')
        meses.clear()
        meses.send_keys(mes)

        ContinuarPag3 = driver.find_element_by_id('baceptar')
        ContinuarPag3.click()

        self.page4(id)

    def page4(self,id):
        
        driver = self.driver

        certificado = driver.find_element_by_id('certI').send_keys(var.PATH_CERTIFICADO)
        time.sleep(5)
        clave_privada = driver.find_element_by_id('keyI').send_keys(var.PATH_CLAVE_PRIVADA)
        time.sleep(5)
        
        ContraPriv = driver.find_element_by_id('keyP')
        ContraPriv.send_keys(var.CONTRASENIA_PRIVADA)

        time.sleep(10)

        Identificarse = driver.find_element_by_xpath('//*[@id="formfirmar"]/table[2]/tbody/tr[3]/td/input')
        Identificarse.click()
        self.page5(id)

    def page5(self, id):
        driver = self.driver

        descargar = driver.find_element_by_xpath('//*[@id="workingContainer"]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/input')
        descargar.click()

        
        time.sleep(10)
        

        ContinuarPag4 = driver.find_element_by_id('btnFirma')
        ContinuarPag4.click()

    #Salida de la prueba
    def tear_Down(self):
        self.driver.quit()

#if __name__ == "__main__":
    #unittest.main(verbosity=2)
