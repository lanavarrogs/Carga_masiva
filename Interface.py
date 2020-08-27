from tkinter import *
from tkinter import filedialog
import main

class Interface:
    
    def _init_(self,root):
        self.miFrame=Frame(raiz, width= 1200, height=600)
        self.miFrame.pack()
        self.create_TextBox()
        self.create_Buttons()
    
    
    def create_Buttons():
        ContrasenaLabel=Label(self.miFrame, text='Busca el archivo de Excel: ')
        ContrasenaLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10 )
        BusExc=Button(self.miFrame, text='Buscar', command=abreExcel)
        BusExc.grid(row=3, column=1)

        CertificadoLabel=Label(self.miFrame, text='Busca el archivo de Certificado: ')
        CertificadoLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10 )
        BusCer=Button(self.miFrame, text='Buscar', command=abreCertificado)
        BusCer.grid(row=4, column=1)

        KeyLabel=Label(self.miFrame, text='Busca el archivo Key: ')
        KeyLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10 )
        BusCer=Button(self.miFrame, text='Buscar', command=abreKey)
        BusCer.grid(row=5, column=1)

        Enviar = Button(self.miFrame, text='Enviar', command=valor)
        Enviar.grid(row=7, column= 1,padx=10, pady=10)

    def create_TextBox():
        nombreLabel=Label(self.miFrame, text='Usuario: ')
        nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)
        cuadroTexto = Entry(self.miFrame)
        cuadroTexto.grid(row=1, column=1, padx=10, pady=10)

        ContrasenaLabel=Label(self.miFrame, text='Contraseña: ')
        ContrasenaLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10 )
        cuadroTextoContrasena = Entry(self.miFrame)
        cuadroTextoContrasena.grid(row=2, column=1, padx=10, pady=10)
        cuadroTextoContrasena.config(show="*")

        ContrasenaLlaveLabel=Label(self.miFrame, text='Contraseña de llave electronica: ')
        ContrasenaLlaveLabel.grid(row=6, column=0, sticky='e', padx=10, pady=10 )
        cuadroTextoContrasenaLlave = Entry(self.miFrame)
        cuadroTextoContrasenaLlave.grid(row=6, column=1, padx=10, pady=10)
        cuadroTextoContrasenaLlave.config(show="*")
    

    def abreExcel(): 
        AbrExe=filedialog.askopenfilename(initialdir = "/",title = "Seleccionar Excel",filetypes = (("Archivos Excel",".xlsx"),("all files",".*")))
        print(AbrExe)

    def abreCertificado():
        AbrCer=filedialog.askopenfilename(initialdir = "/",title = "Selecccionar Certificado",filetypes = (("Archivos Certificado",".cer"),("all files",".*")))
        print(AbrCer)

    def abreKey():
        Abrk=filedialog.askopenfilename(initialdir = "/",title = "Seleccionar Key",filetypes = (("Archivos key",".key"),("all files",".*")))
        print(abreKey)