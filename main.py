from jugador import Jugador
from mago import mago
from guerrero import guerrero
from objeto import objeto
import os 

os.system('cls')

#Método principal
def main():
    
    #crear Jugador
    nuevo_jugador = Jugador("vixoxo")

    #crear Personaje
    magician = mago(" SUKUNA", 10, 100, 80)
    guerricia = guerrero(" TOJI", 10, 100, 75)
    
    #asociar jugador con el personaje
    nuevo_jugador.seleccionar_personaje(guerricia)
    nuevo_jugador.seleccionar_personaje(magician)
    nuevo_jugador.mostrar_perso()

    #ataque del magicimo
    magician.atacar()

    #crear objeto
    pocion = objeto("pocion de vida", "consumible")
    relicario = objeto("relicario maldito", "arma")

    hamburguesa = objeto("hamburguesa del bk", "consumible")
    espada = objeto("katana de alma dividida", "arma")
    #agregar al inventario
    magician.inventario.agregar_obj(pocion)
    magician.inventario.agregar_obj(relicario)

    guerricia.inventario.agregar_obj(hamburguesa)
    guerricia.inventario.agregar_obj(espada)
    
    #mostrar inventario
    magician.inventario.mostrar_invent()

    guerricia.inventario.mostrar_invent()

    #ataque del guerricia
    guerricia.atacar()

if __name__ == "__main__":
    main()
