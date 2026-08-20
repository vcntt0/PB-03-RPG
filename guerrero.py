from personaje import Personaje

class guerrero(Personaje):
    
    def __init__(self, nombre, nivel, vida, fuerza_bruta):
        super().__init__(nombre, nivel, vida)
        self.fuerza_bruta = fuerza_bruta
    
    def atacar(self):
        print(f"{self.nombre} te pego el meo combo xoro"
              f" con {self.fuerza_bruta} de fuerza")