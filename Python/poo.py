# creacion de clases
class Persona():
    pass #no significa nada, si no es para dejar en blanco
    texto=''

    def __init__(self,nombre): #es el contructor y como argumento mando la clase propia y los atributos
        self.nombre= nombre #self sería como el this en java

    def saludar(self):
        self.texto="Hola, mi nombre es" + self.nombre
        return self.texto




class Adulto(Persona): #herencia, hereda métodos y atributos
    def __init__(self,nombre):
        Persona.__init(self,nombre) #llamo al constructor del super


    def saludar(self): #estaria haciendo override de Persona()
        self.texto= "Hola, soy adulto"
        return self.adulto

    def grabar_tarjeta(self,tarjeta): #nuevos metodos que solo pertenecen a la clase Adulto
        self.tarjeta=tarjeta

    def __str__(self):
        self.texto= "Adulto: nombre= " + self.nombre #str es como un toString()
