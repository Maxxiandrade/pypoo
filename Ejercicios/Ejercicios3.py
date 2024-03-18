class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    def __repr__(self):
            return f"{self.nombre} tiene {self.fuerza} puntos de fuerza y {self.velocidad} puntos de velocidad"
    def __add__(self, otro):
        nuevo_nombre = self.nombre + ', ' + otro.nombre
        nueva_fuerza = self.fuerza + otro.fuerza
        nueva_velocidad = self.velocidad + otro.velocidad
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
        
personaje1 = Personaje('Goku', 100, 50)
personaje2 = Personaje('Vegeta', 50, 100)
personaje3 = Personaje('Jiren',100,100)

gogeta = personaje1 + personaje2 + personaje3


print(gogeta) 