#SRP. Single Responsability Principle. Cada clase se ocupa de lo suyo, no le encargamos todas las tareas a una clase

class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            return (f'el tanque tiene {self.tanque.obtener_combustible()} litros')
        else:
            print('No hay suficiente combustible')
    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self,cantidad):
        self.combustible+=cantidad
    def usar_combustible(self, cantidad):
         self.combustible -= cantidad
    def obtener_combustible(self):
        return self.combustible
    
    
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())