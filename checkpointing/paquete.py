class Paquete:
    def __init__(self, id:int, origen:str, destino:str, peso:float): #constructor con sus atributos
        self.__id = id #_protegida
        self.__origen = origen #__privada
        self.__destino = destino #pública
        self.__peso = peso
    
    @property
    def id(self):
        return self.__id
    
    @property
    def origen(self):
        return self.__origen
    
    @property
    def destino(self):
        return self.__destino

    @property
    def peso(self):
        return self.__peso

    def imprimir(self):
        print("Id: ", self.__id)
        print("Origen: ", self.__origen)
        print("Destino: ", self.__destino)
        print("Peso: ", self.__peso)
        print("----------------------------")
 
