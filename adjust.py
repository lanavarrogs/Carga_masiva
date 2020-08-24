import os 
import subprocess

#Buscar el archivo en descargas 
boleta_file = '/home/lanavarrog/Downloads/Boleta.pdf'
destino = './archivos'

def move_files():
    if ( os.path.isdir('./archivos') ):
        if(os.path.isfile(boleta_file)):
            print('holi')
    else:
        os.mkdir('./archivos')


