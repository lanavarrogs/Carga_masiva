import pandas as pd


#importacion del dataset de excel
path_file = './Libro31.xlsx'
dataset = pd.read_excel(path_file)

#Lectura de los datos
def read_RFC():
    #Filtrar el dataframe
    list_rfc = list(dataset['RFC'])
    list_rfc.remove('XAXX010101000')
    print(list_rfc) 

if __name__ == "__main__":
    read_RFC()