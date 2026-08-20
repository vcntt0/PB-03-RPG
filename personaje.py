from inventario import inventario

# clase Personaje

class Personaje:
    
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario = inventario()

    def atacar(self):
        print(f"{self.nombre} realiza un ataque.")
        
    def recibir_danio(self, danio):
        
        self.vida -= danio
        #self.vida = self.vida - danio
        #(esto es lo mismo que arriba pero no simplificado)
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibio {danio} puntos de daño")
        print(f"vida actual {self.vida}")

    def mostrar_danio(self):
        print("\n---INFORMACION DEL COMPARE---")
        print(f"Nombre: {self.nombre}")
        print(f"vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
