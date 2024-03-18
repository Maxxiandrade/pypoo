class A:
    def hablar(self):
        print('Hola desde A')
        
class B(A):
    def hablar(self):
        print('Hola desde B')
        
class C(A):
    def hablar(self):
        print('Hola desde C')
        
class D(B,C):
    def hablar(self):
        print('Hola desde D') #Si borramos esto (pass), imprime desde B. Si borramos B, imprime desde C. Si borramos C, imprime desde A
                              #Esto porque en los parametros le indicamos que primero esta b y despues c (B,C) y si no la encuentra en esas busca en A, que es la clase padre de B y C
d = D()

d.hablar()
print(D.mro())
B.hablar(A)