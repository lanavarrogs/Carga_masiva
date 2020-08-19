
class Persona():
    #Constructor de Persona con los valores del Excel
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno,curp,fecha_inicio,serie,instrumento,fecha_fin,meses,folio_electronico):
        self.__nombre = nombre
        self.__apellioPaterno  = apellidoPaterno
        self.__apellidoMaterno  = apellidoMaterno
        self.__curp = curp
        self.__fecha_inicio = fecha_inicio
        self.__serie = serie
        self.__instrumento  = instrumento
        self.__fecha_fin = fecha_fin
        self.__meses = meses
        self.__folio_electronico = folio_electronico

    #Metodos GETTERS de los atributos de personas

    #Regresar el nombre
    def get_nombre(self):
        return self.__nombre
    #Regresar el apellido paterno
    def get_Apellido_Paterno(self):
        return self.__apellioPaterno 
    #Regresar el apellido Materno
    def get_Apellido_Materno(self):
        return self.__apellidoMaterno
    #Regresar el curp
    def get_Curp(self):
        return self.__curp
    #Regresar la fecha de inicio
    def get_Fecha_Inicio(self):
        return self.__fecha_inicio
    #Regresa el nuero de serie
    def get_Serie(self):
        return self.__serie
    #Regresa el instrumento
    def get_Instrumento(self):
        return self.__instrumento
    #Regresa la fecha final
    def get_Fecha_Fin(self):
        return self.__fecha_fin
    #Regresa los meses
    def get_Meses(self):
        return self.__meses
    #Regresa el folio_Electronico
    def get_Folio_Electrionico(self):
        return self.__folio_electronico


    #SETTERS de Persona

    #Cambia el nombre
    def set_Nombre(self,nombre):
        self.__nombre = nombre
    #Cambia el apellido Paterno
    def set_Apellido_Paterno(self,apellidoPaterno):
        self.__apellioPaterno = apellidoPaterno
    #Cambia el apellido Materno
    def set_Apellido_Materno(self,apellidoMaterno):
        self.__apellioMaterno = apellidoMaterno
    #Cambia el curp
    def set_Curp(self,curp):
        self.__curp = curp
    #Cambia la fecha de inicio
    def set_Fecha_Inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    #Cambia el numero de serie
    def set_Serie(self,serie):
        self.__serie = serie
    #Cambia el Instrumento 
    def set_Instrumento(self,instrumento):
        self.__instrumento = instrumento
    #Cambia la fecha final
    def set_Fecha_Fin(self,fecha_fin):
        self.__fecha_fin = fecha_fin
    #Cambia los meses
    def set_Meses(self,meses):
        self.__meses = meses
    #Cambia el folio electronico
    def set_Folio_Electsronico(self,folio_electronico):
        self.__folio_electronico = folio_electronico