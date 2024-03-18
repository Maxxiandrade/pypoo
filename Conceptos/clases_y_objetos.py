
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        print(f'Estas llamando desde un {self.modelo}')

celular1 = Celular("Apple", "15Pro", "48MP")

celular1.llamar()