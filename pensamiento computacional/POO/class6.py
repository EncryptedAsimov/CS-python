### Herencia ###
#pérmite modelar una jerarquia de clases
#permite compartir comportamiento comun en la jerarquia
#Al padre se le conoce como una superclase y al hijo como subclase

#Example:
## jerarquia de vehiculos ##
#los vehiculos pueden moverse,frenar, avanzar
#hay vehiculos terrestres y aereos
#hay vehiculos recreativos y otros no, hay infitas ramificaciones

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado,lado) #funcion que obtiene la referencia directa al constructor de la superclase

if __name__ == "__main__":
    rectangulo = Rectangulo(base= 3, altura= 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area()) #heredamos el metodo area de la superclase
