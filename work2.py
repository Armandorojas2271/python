from abc import ABC, abstractmethod

class Persona(ABC):
    '''Clase abstracta que representa una persona'''
    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Apellido: {self.apellido}"

class Alumno(Persona):
    '''Clase que representa a un alumno.'''
    def __init__(self, cedula, nombre, apellido, carrera):
        # llamamos al constructor de Persona
        super().__init__(cedula, nombre, apellido)
        # agregamos el nuevo atributo
        self.carrera = carrera
    
    def __str__(self):
        return f"{super().__str__()}, Carrera: {self.carrera}"

if __name__ == '__main__':
    # Crear un objeto del tipo Alumno con nombre "Armando Ojeda"
    alumno1 = Alumno("6797518", "Armando", "Ojeda", "Ingeniería informatica")
    # Imprimir sus datos
    print(alumno1)
