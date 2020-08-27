import os 
import subprocess
import getpass

#Obtener el usuario
usr = getpass.getus()
#Buscar el archivo en descargas 
boleta_file = 'C:\Users\{}}\OneDrive\Descargas\Boleta.pdf'
destino = './archivos'

def move_files():
    if ( os.path.isdir('./archivos') ):
        if(os.path.isfile(boleta_file)):
            print('holi')
    else:
        os.mkdir('./archivos')


