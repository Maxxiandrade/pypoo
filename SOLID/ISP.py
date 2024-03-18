#ISP. Interface Segregation Principle. Ningun cliente tiene que ser forzado a depender de interfaces que no utilice
#En este caso, con interfaz nos refermimos a clases abstractas


from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    
    # @abstractclassmethod
    # def comer(self):
    #     pass
    
    @abstractclassmethod                    
    def trabajar(self):
        pass
    
    # @abstractclassmethod
    # def dormir(self):
    #     pass
 
class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass
    
class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
    
class Humano(Trabajador,Durmiente, Comedor):
    
     def comer(self):
        print('El humano está comiendo')

     def trabajar(self):
        print('El humano está trabajando')
    
     def dormir(self):
        print('El humano esta durmiendo')


class Robot(Trabajador):
    
     def trabajar(self):
        print('El robot está trabajando')
