from paquete import Paquete
from os import system

def clear():
    input()
    system('cls')

class Paqueteria:
    def __init__(self, lista:list):
        self.__lista = lista

    def agregar(self, paquete:Paquete):
        try:
            if paquete.id <= 0 or paquete.peso <= 0: # no podemos aceptar que un ID o el peso sea 0 o negativo
                raise ValueError("La cantidad tiene que ser positiva e indiferente de cero.") # alzamos el error de valor
            if not self.esCopia(paquete):
                self.__lista.append(paquete)
                return True
        except ValueError as v:
            print(v) # si es que hizo el error
            return False
    

    def rastrear(self):
        try:
            i = 0  # imitación de la función retry
            while i != 3:
                id = int(input("Id a rastrear: "))
                for p in self.__lista:
                    if id == p.id:
                        p.imprimir()
                        return
                i += 1
                print("No se encontró, intenta otra vez")
                clear()
                
            if i == 3:
                raise Exception("Ya intentaste 3 veces")       
        except Exception as v:
            print(v)
            
        

        
    
    def mostrar(self):
        for p in self.__lista:
            p.imprimir()
    
    def vacia(self):
        if len(self.__lista) == 0:
            return True
        else:
            return False
    
    def respaldar(self):
        archivo = open("file.txt", "w+")
        for p in self.__lista:
            archivo.write(f"Id: {p.id}\n")
            archivo.write(f"Origen: {p.origen}\n")
            archivo.write(f"Destino: {p.destino}\n")
            archivo.write(f"Peso: {p.peso}\n")
        archivo.close()
    
    def esCopia(self, p:Paquete):
        try:
            for paquete in self.__lista:
                if p.id == paquete.id:
                    raise ValueError("Ya hay un elemento con el mismo ID")
            return False
        except ValueError as v:
            print(v)
            return True