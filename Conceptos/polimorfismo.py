class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
perro = Perro()
gato = Gato()

hacer_sonido(perro)

print(gato.sonido())