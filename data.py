import pandas as pd
import numpy as np
from datetime import datetime
import main


DireccionExcel = main.abreExcel()
#importacion del dataset de excel
path_file = DireccionExcel
dataset = pd.read_excel(path_file)

#Rellenando los na
dataset = dataset.replace(np.nan,'',regex=True)

#Lectura del RFC
def read_RFC(id):
    #Filtrar el dataframe obteniendo los RFC
    list_rfc = list(dataset['RFC'])
    return list_rfc[id]

#Regresa el folio Electronico
def read_electronic_folio(id):
    electronic_folio = list(dataset['FOLIO ELECTRONICO'])
    return electronic_folio[id]

#Regresa la lista de nombres separadas
def get_name(id):
    fullname = list(dataset['NOMBRE'])
    names = []
    for i in range(0,len(fullname)):
        names.append(fullname[i].split(' '))
    names[id] = [i for i in names[id] if i]
    return names[id]

def get_fecha_inicio(id):
    fecha_inicio = list(dataset['FECHA DE INI'])
    date_inicio = fecha_inicio[id].strftime('%d''/''%m''/''%Y')
    return date_inicio

def get_fecha_fin(id):
    fecha_inicio = list(dataset['FECHA FIN'])
    date_fin = fecha_inicio[id].strftime('%d''/''%m''/''%Y')
    return date_fin

def get_monto_credito(id):
    monto_inicio = list(dataset['MONTO CREDITO'])
    return monto_inicio[id]


def read_CURP(id):
    curp = list(dataset['CURP'])
    return curp[id]

def get_no_serie(id):
    serie =  list(dataset['serie'])
    return serie[id]

def get_month(id):
    month = list(dataset['MESES'])
    return (round(month[id]))

def data_length():
    return len(dataset)
    

if __name__ == "__main__":
    get_month(1)


    """ boton se sigiente 
        firma optenida
        algoritmo de descarga"""