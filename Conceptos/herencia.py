class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
            

roberto = Empleado('Maxi', 23, 'argentino', 'programador', 1000)

print(roberto.salario)



class Galletita:
    def __init__(self, ingredientes):
        [self.ingrediente1, self.ingrediente2] = ingredientes
    
    def cocinar(self):
        print(f'Haciendo una galletita con {self.ingrediente1} y {self.ingrediente2}')
    
    def resultado(self):
        return(f'Galletita con {self.ingrediente1} y {self.ingrediente2}')
        

class Desayuno(Galletita):
    def __init__(self, ingredientes, bebida):
        super().__init__(ingredientes)
        self.bebida = bebida
    def desayunar(self):
        print(f'Desayunando una {self.resultado()} con {self.bebida}')

galletita_de_avena_y_pasas = Galletita(["avena","pasas"])

galletita_de_avena_y_pasas.cocinar()
galletita_de_avena_y_pasas.resultado()


desayuno_con_leche = Desayuno(["avena","pasas"],'Leche')

desayuno_con_leche.desayunar()


#Herencia multiple

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f'Mi habilidad es {self.habilidad}')
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        return (f'{super().mostrar_habilidad()}') # -> Muestra la habilidad de la clase QUE ESTA HEREDANDO
        #return (f'{self().mostrar_habilidad()}') -> Muestra la habilidad de ESTA clase
    
    
jose = EmpleadoArtista('Jose', 23, "argentino", "cantar", "programador", 100000)

jose.presentarse()

#Verificar si es subclase de 
herencia = issubclass(EmpleadoArtista,Persona)
print(herencia)

#Verificar si es instancia de
instancia = isinstance(jose,EmpleadoArtista)
print(instancia)