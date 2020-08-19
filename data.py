import pandas as pd
import numpy as np

#importacion del dataset de excel
path_file = './Libro31.xlsx'
dataset = pd.read_excel(path_file)

#Rellenando los na
dataset = dataset.replace(np.nan,'',regex=True)

#Lectura del RFC
def read_RFC(id):
    #Filtrar el dataframe obteniendo los RFC
    list_rfc = list(dataset['RFC'])
    print(list_rfc[id])

#Regresa el folio Electronico
def read_electronic_folio(id):
    electronic_folio = list(dataset['FOLIO ELECTRONICO'])
    return electronic_folio[id]

#Regresa la lista de nombres separadas
def get_name(id):
    fullname = list(dataset['NOMBRE'])
    print(fullname[id].split(' ') )

def data_length():
    return len(dataset)


