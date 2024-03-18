def decorador(fn):
    def fn_modificada():
        print('Antes de llamar a la funcion')
        fn()
        print('Despues de llamar a la funcion')
    return fn_modificada


def saludar():
    return print('Holaa')

decorador(saludar)

@decorador
def saludo():
    print('Hola')
    
saludo()