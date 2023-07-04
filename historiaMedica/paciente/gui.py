import tkinter as tk
from modelo.pacienteDao import Persona, guardarDatoPaciente

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.camposPaciente()
        self.deshabilitar()
        

    def camposPaciente(self):

        #LABELS

        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)    

        self.lblApellido = tk.Label(self, text='Apellido: ')
        self.lblApellido.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblApellido.grid(column=0, row=1, padx=10, pady=5)

        self.lblDni = tk.Label(self, text='DNI: ')
        self.lblDni.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblDni.grid(column=0, row=2, padx=10, pady=5)

        self.lblFechaDeNacimiento = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechaDeNacimiento.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblFechaDeNacimiento.grid(column=0, row=3, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=4, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Teléfono: ')
        self.lblTelefono.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=5, padx=10, pady=5)

        self.lblProfesion = tk.Label(self, text='Profesión: ')
        self.lblProfesion.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblProfesion.grid(column=0, row=6, padx=10, pady=5)

        self.lblApp = tk.Label(self, text='APP: ')
        self.lblApp.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblApp.grid(column=0, row=7, padx=10, pady=5)

        self.lblApq = tk.Label(self, text='APQ: ')
        self.lblApq.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblApq.grid(column=0, row=8, padx=10, pady=5)

        self.lblToxicos = tk.Label(self, text='Tóxicos: ')
        self.lblToxicos.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblToxicos.grid(column=0, row=9, padx=10, pady=5)

        self.lblAlergias = tk.Label(self, text='Alergias: ')
        self.lblAlergias.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblAlergias.grid(column=0, row=10, padx=10, pady=5)

        self.lblMedicamentos = tk.Label(self, text='Medicamentos: ')
        self.lblMedicamentos.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblMedicamentos.grid(column=0, row=11, padx=10, pady=5)

        self.lblDieta = tk.Label(self, text='Dieta: ')
        self.lblDieta.config(font=('ARIAL',15, 'bold'), bg='#CDD8FF')
        self.lblDieta.grid(column=0, row=12, padx=10, pady=5)

        #ENTRIES

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL', 15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellido = tk.StringVar()
        self.entryApellido = tk.Entry(self, textvariable=self.svApellido)
        self.entryApellido.config(width=50, font=('ARIAL', 15))
        self.entryApellido.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL', 15))
        self.entryDni.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFechaDeNacimiento = tk.StringVar()
        self.entryFechaDeNacimiento = tk.Entry(self, textvariable=self.svFechaDeNacimiento)
        self.entryFechaDeNacimiento.config(width=50, font=('ARIAL', 15))
        self.entryFechaDeNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL', 15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL', 15))
        self.entryTelefono.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svProfesion = tk.StringVar()
        self.entryProfesion = tk.Entry(self, textvariable=self.svProfesion)
        self.entryProfesion.config(width=50, font=('ARIAL', 15))
        self.entryProfesion.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svApp = tk.StringVar()
        self.entryApp = tk.Entry(self, textvariable=self.svApp)
        self.entryApp.config(width=50, font=('ARIAL', 15))
        self.entryApp.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svApq = tk.StringVar()
        self.entryApq = tk.Entry(self, textvariable=self.svApq)
        self.entryApq.config(width=50, font=('ARIAL', 15))
        self.entryApq.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.svToxicos = tk.StringVar()
        self.entryToxicos = tk.Entry(self, textvariable=self.svToxicos)
        self.entryToxicos.config(width=50, font=('ARIAL', 15))
        self.entryToxicos.grid(column=1, row=9, padx=10, pady=5, columnspan=2)

        self.svAlergias = tk.StringVar()
        self.entryAlergias = tk.Entry(self, textvariable=self.svAlergias)
        self.entryAlergias.config(width=50, font=('ARIAL', 15))
        self.entryAlergias.grid(column=1, row=10, padx=10, pady=5, columnspan=2)

        self.svMedicamentos = tk.StringVar()
        self.entryMedicamentos = tk.Entry(self, textvariable=self.svMedicamentos)
        self.entryMedicamentos.config(width=50, font=('ARIAL', 15))
        self.entryMedicamentos.grid(column=1, row=11, padx=10, pady=5, columnspan=2)

        self.svDieta = tk.StringVar()
        self.entryDieta = tk.Entry(self, textvariable=self.svDieta)
        self.entryDieta.config(width=50, font=('ARIAL', 15))
        self.entryDieta.grid(column=1, row=12, padx=10, pady=5, columnspan=2)

        #BUTTONS

        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=14, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#000000', cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=14, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6',
                             bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=14, padx=10, pady=5)

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApellido.get(), self.svDni.get(), self.svFechaDeNacimiento.get(), self.svEdad.get(),
            self.svTelefono.get(), self.svProfesion.get(), self.svApp.get(), self.svApq.get(), self.svToxicos.get(),
            self.svAlergias.get(), self.svMedicamentos.get(), self.svDieta.get()
        )    

        guardarDatoPaciente(persona)
        self.deshabilitar()

    def habilitar(self):
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDni.set('')
        self.svFechaDeNacimiento.set('')
        self.svEdad.set('')
        self.svTelefono.set('')
        self.svProfesion.set('')
        self.svApp.set('')
        self.svApq.set('')
        self.svToxicos.set('')
        self.svAlergias.set('')
        self.svMedicamentos.set('')
        self.svDieta.set('')   

        self.entryNombre.config(state='normal')
        self.entryApellido.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFechaDeNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryTelefono.config(state='normal')
        self.entryProfesion.config(state='normal')
        self.entryApp.config(state='normal')
        self.entryApq.config(state='normal')
        self.entryToxicos.config(state='normal')
        self.entryAlergias.config(state='normal')
        self.entryMedicamentos.config(state='normal')
        self.entryDieta.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')


    def deshabilitar(self):
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDni.set('')
        self.svFechaDeNacimiento.set('')
        self.svEdad.set('')
        self.svTelefono.set('')
        self.svProfesion.set('')
        self.svApp.set('')
        self.svApq.set('')
        self.svToxicos.set('')
        self.svAlergias.set('')
        self.svMedicamentos.set('')
        self.svDieta.set('')   

        self.entryNombre.config(state='disabled')
        self.entryApellido.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFechaDeNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        self.entryProfesion.config(state='disabled')
        self.entryApp.config(state='disabled')
        self.entryApq.config(state='disabled')
        self.entryToxicos.config(state='disabled')
        self.entryAlergias.config(state='disabled')
        self.entryMedicamentos.config(state='disabled')
        self.entryDieta.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
