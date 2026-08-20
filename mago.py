from personaje import Personaje

class mago(Personaje):
    
    def __init__(self, nombre, nivel, vida, poder_magico):
        super().__init__(nombre, nivel, vida)
        self.poder_magico = poder_magico
    
    def atacar(self):
        print(f"{self.nombre} lanzo el meo poder xoro"
              f" con {self.poder_magico} de poder magico")
        