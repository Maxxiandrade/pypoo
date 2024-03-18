# Crea un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y estudiante. La clase Persona tendrá los atributos nombre y edad y un metodo que
# imprima el nombre y la edad de la persona. La clase estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def imprime_nombre(self):
        return print(f'{self.nombre} tiene {self.edad} años')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def imprime_grado(self):
        print(f'{self.nombre} va a {self.grado} grado')
        
estudiante = Estudiante('Maxi', 23, '7mo')

estudiante.imprime_nombre()
estudiante.imprime_grado()


# Imagina que estas modelando animales en un zoologico. Crear 3 clases: "Animal", "Mamifero" y "Ave". La clase "Animal" debe tener un método llamado "comer". La clase "Mamifero" debe tener
# un método llamado "amamantar" y la clase "Ave" un método llamado "volar".

# Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", ademas de "comer"

class Animal:
        def comer(self):
            print('Está comiendo..')
        
class Mamifero(Animal):
        def amamantar(self):
            print('Está amamantando..')
        
class Ave(Animal):
        def volar(self):
            print('Puede volar')
        
        
class Murcielago(Mamifero, Ave):
        pass
            
murcielago = Murcielago()

murcielago.amamantar()
murcielago.volar()
murcielago.comer()

Murcielago.mro()