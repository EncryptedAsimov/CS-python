#abstracción enfoque en informaión relevante
#separar inf central de detalles secundarios
#utilizacion de variables privads...
#Cómo se inyecta la gasolina? No sabemos y tampoco es relevante
#pensar que es publico y que es privado

class Lavadora:
    def __init__(self):
        pass

    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self,temperatura):
        print(f'llenando el tanque con agua en temperatura de {temperatura}')

    def _añadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('lavando')

    def _centrifugar(self):
        print('centrifugando')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()