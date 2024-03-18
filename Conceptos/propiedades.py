
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    @property
    def nombre(self): #Getter
        return self.__nombre
    @nombre.setter
    def nombre(self, new_nombre): #Setter
        self.__nombre = new_nombre 
        
    @nombre.deleter
    def nombre(self, new_nombre): #Deleter
        self.__nombre = new_nombre 
    
maxi = Persona('Maxi',23)


nombre = maxi.nombre
print(nombre)

nombre = 'Maximiliano'
print(nombre)

del maxi.nombre
print(nombre)
