#Definition
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_persona):
        print(f'Hola {otra_persona.nombre} me llamo {self.nombre}')
    def get_nombre(self):
        return self.nombre

#uso 

david = Persona('David', 34)
erika = Persona('Erika', 50)

print(david.get_nombre())
david.saluda(erika)