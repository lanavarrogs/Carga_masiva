from tkinter import *
from tkinter import filedialog
import main
import unittest



class Interface:
    
    def __init__(self,root):
        self.miFrame=Frame(root, width= 1200, height=600)
        self.miFrame.pack()
        self.create_TextBox()
        self.create_Buttons()
        self.get_correo()
    
    
    def create_Buttons(self):
        ContrasenaLabel=Label(self.miFrame, text='Busca el archivo de Excel: ')
        ContrasenaLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10 )
        BusExc=Button(self.miFrame, text='Buscar', command=self.abreExcel)
        BusExc.grid(row=3, column=1)

        CertificadoLabel=Label(self.miFrame, text='Busca el archivo de Certificado: ')
        CertificadoLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10 )
        BusCer=Button(self.miFrame, text='Buscar', command=self.abreCertificado)
        BusCer.grid(row=4, column=1)

        KeyLabel=Label(self.miFrame, text='Busca el archivo Key: ')
        KeyLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10 )
        BusCer=Button(self.miFrame, text='Buscar', command=self.abreKey)
        BusCer.grid(row=5, column=1)

        Enviar = Button(self.miFrame, text='Enviar', command=self.valor)
        Enviar.grid(row=7, column= 1,padx=10, pady=10, sticky=W + E)

    def create_TextBox(self):
        self.nombreLabel=Label(self.miFrame, text='Usuario: ')
        self.nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)
        self.cuadroTexto = Entry(self.miFrame)
        self.cuadroTexto.focus()
        self.cuadroTexto.grid(row=1, column=1, padx=10, pady=10)

        self.ContrasenaLabel=Label(self.miFrame, text='Contraseña: ')
        self.ContrasenaLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10 )
        self.cuadroTextoContrasena = Entry(self.miFrame)
        self.cuadroTextoContrasena.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroTextoContrasena.config(show="*")

        self.ContrasenaLlaveLabel=Label(self.miFrame, text='Contraseña de llave electronica: ')
        self.ContrasenaLlaveLabel.grid(row=6, column=0, sticky='e', padx=10, pady=10 )
        self.cuadroTextoContrasenaLlave = Entry(self.miFrame)
        self.cuadroTextoContrasenaLlave.grid(row=6, column=1, padx=10, pady=10)
        self.cuadroTextoContrasenaLlave.config(show="*")
    
    def get_correo(self):
        return self.cuadroTexto.get()

    def get_contrasenia(self):
        return self.cuadroTextoContrasena.get()

    def abreExcel(self):
        AbrExe=filedialog.askopenfilename(initialdir = "/",title = "Seleccionar Excel",filetypes = (("Archivos Excel",".xlsx"),("all files",".*")))
        print(AbrExe)

    def abreCertificado(self):
        AbrCer=filedialog.askopenfilename(initialdir = "/",title = "Selecccionar Certificado",filetypes = (("Archivos Certificado",".cer"),("all files",".*")))
        print(AbrCer)

    def abreKey(self):
        Abrk=filedialog.askopenfilename(initialdir = "/",title = "Seleccionar Key",filetypes = (("Archivos key",".key"),("all files",".*")))
        print(abreKey)
    
    def valor(self):
        unittest.main(verbosity=2)