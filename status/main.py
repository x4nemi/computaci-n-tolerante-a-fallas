from paqueteria import Paqueteria
from paquete import Paquete
from hilo import SerializarHilo
from os import system
import pickle
import os

def clear():
    input()
    system('cls')

def cadenaVacia(cadena):
    if len(cadena) == 0:
        return True
    return False


def menu(p:Paqueteria):
    while True:
        print("1) Agregar")
        print("2) Mostrar")
        print("3) Respaldar")
        print("4) Rastrear")
        print("0) Salir")
        op = input("Opcion: ")

        if (op == "2" or op == "3" or op == "4") and p.vacia():
            print("No hay elementos agregados")
            continue

        system('cls')

        if op == "1":
            print("Agregar--------------------------")
            bandera = False
            while not bandera:
                try:
                    hilo = SerializarHilo(p)
                    hilo.start() #
                    id = int(input("Id: "))                        
                    origen = input("Origen: ")
                    destino = input("Destino: ")
                    if cadenaVacia(origen) or cadenaVacia(destino):
                        raise Exception("No puedes dejar la cadena vacia")
                    peso = float(input("Peso: "))

                    paquete = Paquete(id, origen, destino, peso)

                    # listaPaquetes.append(paquete)
                    # print(listaPaquetes)
                    # pickledPaquete = pickle.dumps(listaPaquetes)
                    # pickle_out = open("paqueteria", "wb")
                    # pickle.dump(pickledPaquete, pickle_out)
                    # pickle_out.close()
                    if p.agregar(paquete): # sólo se agrega si se se escriben bien los parámetros
                        print("Agregado...")
                        bandera = True
                        hilo.stop()
                    else:
                        clear()

                except:
                    print("ID-Entero, Origen y Destino-Cadena, Peso-Real")
                
                finally:
                    hilo.stop()
                

        elif op == "2":
            print("Mostrar paquetes-----------------")
            p.mostrar()

        elif op == "0":
            print("Adios")
            break

        elif op == "3":
            try:
                p.respaldar()
                print("Respaldado...")
            except:
                print("Error en el archivo al respaldar")
        
        elif op == "4":
            p.rastrear()

        else:
            print("Esa opcion no existe")    
        
        clear()

def agregarPaquete(p:Paqueteria):
    id = int(input("Id: "))                        
    origen = input("Origen: ")
    destino = input("Destino: ")
    if cadenaVacia(origen) or cadenaVacia(destino):
        raise Exception("No puedes dejar la cadena vacia")
    peso = float(input("Peso: "))

    paquete = Paquete(id, origen, destino, peso)


p = Paqueteria()



if os.path.exists("paqueterias"):
    tam_archivo = os.stat("paqueterias").st_size # el archivo debe tener algo
    if tam_archivo != 0:
        print("Quieres reestablecer lo que habías guardado anteriormente? (S/N)")
        respuesta = input(": ")
        
        if respuesta.lower() == "n":
            menu(p)
        
        elif respuesta.lower() == "s":
            
            try:
                pickle_in = open("paqueterias", "rb")
                #lista = pickle.load(pickle_in)
                paqueteria = pickle.load(pickle_in)
                pickle_in.close()
                menu(paqueteria)

            except:
                raise Exception("Error al respaldar")
            
            finally:
                pickle_in.close()
        
        else:
            print("Bye")
    else:
        menu(p)

else:
    menu(p)