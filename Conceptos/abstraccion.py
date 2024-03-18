class Auto:
    def __init__(self):
        self._estado = 'apagado'
    def encender(self):
        self._estado = 'encendido'
        print('El auto esta encendido')
    def conducir(self):
        if(self._estado == 'apagado'):
            print('Encendiendo el auto..')
            self.encender()
        print('Conduciendo el auto')
        
mi_auto = Auto()

mi_auto.conducir()

#El usuario no sabe todo lo que pasa atras de conduccion, no sabe que verificamos si el auto esta encendido, y si esta apago lo encendemos