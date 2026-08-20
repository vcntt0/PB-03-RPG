
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personaje = None

    def seleccionar_personaje(self, personaje):
        
        self.personaje = personaje

        print(f"{self.nombre} selecciono al personaje "
              f"{personaje.nombre}")
    
    def mostrar_perso(self):
        if self.personaje is not None:
            print(f"el compare {self.nombre}"
                  f" va a usar al xoro{self.personaje.nombre}")
        else:
            print("no hay pikiao a niuno")

