#Open/Closed Principle - Las clases y todo eso tiene que estar abierto para su extencion pero cerrado para su modificacion
class Notificador():
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.email} vía e-mail")

class NotificadorSms(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.sms} vía SMS")

class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.whatsapp} vía Whatsapp")
        
        
        
class Usuario():
    def __init__(self,nombre,email,numero):
        self.nombre = nombre
        self.email = email
        self.numero = numero
        
        
        
        
        