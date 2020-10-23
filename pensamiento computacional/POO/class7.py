#polimorfismo es la capacidad de tomar varias formas
#en python es muy facil cambiar el comportamiento de la superclase para adaptarlo a una subclase

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    def avanza(self):
        print("Ando caminando")

class Ciclista(Persona): #recordar que se lee "La clase ciclista extiende Persona"
    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Ando moviendome en bicicleta")

def main():
    persona = Persona("David")
    persona.avanza()

    ciclista = Ciclista("Pablo")
    ciclista.avanza()



if __name__ == '__main__':
    main()


