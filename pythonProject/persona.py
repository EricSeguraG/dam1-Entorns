class Persona:
    def __init__(self,nombre_,edad_,ciudad_):
        self.nombre=nombre_
        self.edad=edad_
        self.ciudad=ciudad_
        self.numero_hijos=0

    def mostrar_info(self):
        print(f"nombre:{self.nombre} \nedad:{self.edad} \nciudad:{self.ciudad} \nnumero_hijos:{self.numero_hijos}")

    def actualitzar_edad(self,nueva_edad):
        if nueva_edad<=120 and nueva_edad>0:
         self.edad=nueva_edad
    def actualizar_hijos(self,nuevos_hijos):
        if nuevos_hijos>=0 and nuevos_hijos<=100:
         self.numero_hijos=nuevos_hijos

persona1=Persona ("pedro","45","barcelona")
persona1.actualitzar_edad(150)
persona1.actualizar_hijos(2)
persona1.mostrar_info()

