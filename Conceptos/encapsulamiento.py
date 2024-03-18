class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"  #La forma de darle entender a python que estamos creando un atributo privado es con ._ 
        self.__atributo_privado = "Valor MUY privado"  #La forma de darle entender a python que estamos creando un atributo MUY privado es con .__ 
    def __hablar(self):
        print('Esto va a tirar error porque es MUY privado')
objeto = MiClase()

print(objeto._atributo_privado)


class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    def get_nombre(self): #Getter
        return self.__nombre
    def set_nombre(self, new_nombre): #Setter
        self.__nombre = new_nombre 
    
maxi = Persona('Maxi',23)

nombre = maxi.get_nombre()

maxi.set_nombre('Maximiliano')
nombre = maxi.get_nombre()

print(nombre)