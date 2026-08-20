class inventario:
    def __init__(self):
        self.objeto = []
    
    def agregar_obj(self, objeto):

        self.objeto.append(objeto)
        
        print(f"{objeto.nombre} ha sido agregado al inventario.")

    def mostrar_invent(self):
        print("\n---INVENTARIO---")

        if len(self.objeto) == 0:
            print("no teni nada loji")
        else:
            for objeto in self.objeto:
                print(f"- {objeto.nombre} ({objeto.tipo})")