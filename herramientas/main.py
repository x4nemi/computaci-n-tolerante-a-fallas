from paqueteria import Paqueteria
from paquete import Paquete
from os import system


def clear():
    input()
    system('cls')


def menu():
    p = Paqueteria()
    while True:
        print("1) Agregar")
        print("2) Mostrar")
        print("3) Respaldar")
        print("4) Rastrear")
        print("0) Salir")
        op = input("Opcion: ")

        if op == "2" and p.vacia():
            print("No hay elementos agregados")
            continue

        system('cls')

        if op == "1":
            print("Agregar--------------------------")
            bandera = False
            while not bandera:
                try:
                    id = int(input("Id: "))                        
                    origen = input("Origen: ")
                    destino = input("Destino: ")
                    peso = float(input("Peso: "))

                    paquete = Paquete(id, origen, destino, peso)

                    if p.agregar(paquete):
                        print("Agregado...")
                        bandera = True
                    
                    else:
                        clear()

                except:
                    print("ID-Entero, Origen y Destino-Cadena, Peso-Real")
                

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



menu()