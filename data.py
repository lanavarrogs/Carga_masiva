import pandas as pd
import numpy as np

#importacion del dataset de excel
path_file = './Libro31.xlsx'
dataset = pd.read_excel(path_file)

#Rellenando los na
dataset = dataset.replace(np.nan,'',regex=True)

#Lectura del RFC
def read_RFC():
    #Filtrar el dataframe obteniendo los RFC
    list_rfc = list(dataset['RFC'])
    list_rfc.remove('XAXX010101000')
    return list_rfc

#Regresa el folio Electronico
def read_electronic_folio():
    electronic_folio = list(dataset['FOLIO ELECTRONICO'])
    return electronic_folio

#Regresa la lista de nombres separadas
def get_name():
    fullname = list(dataset['NOMBRE'])
    names  = []
    for i in range(0,len(fullname)):
        names.append(fullname[i].split(' '))
    return names


if __name__ == "__main__":
    read_RFC()
    read_electronic_folio()
    get_name()