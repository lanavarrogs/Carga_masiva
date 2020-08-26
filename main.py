from tkinter import *
from tkinter import filedialog

NomKey = ""

raiz = Tk()
raiz.title('Carga masiva RUG')

miFrame=Frame(raiz, width= 1200, height=600)
miFrame.pack()

nombreLabel=Label(miFrame, text='Usuario: ')
nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)
cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=1, column=1, padx=10, pady=10)

ContrasenaLabel=Label(miFrame, text='Contraseña: ')
ContrasenaLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10 )
cuadroTextoContrasena = Entry(miFrame)
cuadroTextoContrasena.grid(row=2, column=1, padx=10, pady=10)
cuadroTextoContrasena.config(show="*")


def abreExcel(): 
    AbrExe=filedialog.askopenfilename(initialdir = "/",title = "Seleccionar Excel",filetypes = (("Archivos Excel",".xlsx"),("all files",".*")))
    print(AbrExe)

def abreCertificado():
    AbrCer=filedialog.askopenfilename(initialdir = "/",title = "Selecccionar Certificado",filetypes = (("Archivos Certificado",".cer"),("all files",".*")))
    print(AbrCer)

def abreKey():
    Abrk=filedialog.askopenfilename(initialdir = "/",title = "Seleccionar Key",filetypes = (("Archivos key",".key"),("all files",".*")))
    print(abreKey)


ContrasenaLabel=Label(miFrame, text='Busca el archivo de Excel: ')
ContrasenaLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10 )
BusExc=Button(miFrame, text='Buscar', command=abreExcel)
BusExc.grid(row=3, column=1)

CertificadoLabel=Label(miFrame, text='Busca el archivo de Certificado: ')
CertificadoLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10 )
BusCer=Button(miFrame, text='Buscar', command=abreCertificado)
BusCer.grid(row=4, column=1)

KeyLabel=Label(miFrame, text='Busca el archivo Key: ')
KeyLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10 )
BusCer=Button(miFrame, text='Buscar', command=abreKey)
BusCer.grid(row=5, column=1)

#lambda:[self.abreKey(), self.get_name()])

ContrasenaLlaveLabel=Label(miFrame, text='Contraseña de llave electronica: ')
ContrasenaLlaveLabel.grid(row=6, column=0, sticky='e', padx=10, pady=10 )
cuadroTextoContrasenaLlave = Entry(miFrame)
cuadroTextoContrasenaLlave.grid(row=6, column=1, padx=10, pady=10)
cuadroTextoContrasenaLlave.config(show="*")

Enviar = Button(miFrame, text='Enviar', command=abreExcel)
Enviar.grid(row=7, column= 1,padx=10, pady=10)

raiz.mainloop()
