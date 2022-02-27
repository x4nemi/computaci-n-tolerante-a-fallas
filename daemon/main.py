import threading
import time
from persona import Persona
from hilo import Hilo

P = Persona()

def printLoop():
    for i in range(30):
        print(P)
        time.sleep(5)

P.recuperar()
t1 = Hilo(P)
t2 = threading.Thread(target=printLoop)
t1.start()
t2.start()