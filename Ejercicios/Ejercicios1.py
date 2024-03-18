
class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'{self.nombre} está estudiando..')
        
    
nombre = input('Ingrese el nombre del alumno ')
edad = input('Ingrese la edad del alumno ')
grado = input('Ingrese el grado del alumno ')

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre : {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n""")

# while True:
#     estudiar = input()
#     if(estudiar.lower() == "estudiar"):
#         estudiante.estudiar()
        

class ProPlayer:
    def __init__(self, nombre, juego, horas):
        self.nombre = nombre
        self.juego = juego
        self.horas = horas
    def entrenar(self):
        print(f'{self.nombre} entrenó en {self.juego} por {self.horas}')
        
nombre = input('Nombre del player: ')
juego = input(f'A qué va a jugar {nombre}? ')
horas = input('Por cuanto tiempo? ')        

player1 = ProPlayer(nombre, juego, horas)

player1.entrenar()