from conexion import ConexionDB
from tkinter import messagebox

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellido, dni, fechaNacimiento, edad, telefono, profesion, app, apq, toxicos, alergias,
              medicamentos, dieta, activo) VALUES ('{persona.nombre}','{persona.apellido}', {persona.dni},'{persona.fechaNacimiento}',
              {persona.edad},'{persona.telefono}','{persona.profesion}','{persona.app}','{persona.apq}','{persona.toxicos}','{persona.alergias}', 
             '{persona.medicamentos}','{persona.dieta}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showerror(title, mensaje)    

class Persona:
    def __init__(self, nombre, apellido, dni, fechaNacimiento, edad, telefono, profesion, app, apq, toxicos, alergias, medicamentos, dieta):
        self.idPersona = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.telefono = telefono
        self.profesion = profesion
        self.app = app
        self.apq = apq
        self.toxicos = toxicos
        self.alergias = alergias
        self.medicamentos = medicamentos
        self.dieta = dieta

    def __str__(self):
        return f'Persona[{self.nombre}, {self.apellido}, {self.dni}, {self.fechaNacimiento}, {self.edad}, {self.telefono}, {self.profesion}, {self.app}, {self.apq}, {self.toxicos}, {self.alergias}, {self.medicamentos}, {self.dieta}]'    