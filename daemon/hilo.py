from persona import Persona
from threading import Thread
import time

# Clase para el hilo
# Se va a correr mientras se esté guardando, muchas veces
class Hilo(Thread):
    def __init__(self, objeto:Persona):
        Thread.__init__(self)
        self.running = True
        self.objeto = objeto
        self.daemon = True

    def run(self):
        while self.running:
            time.sleep(5)
            self.objeto.recuperar()
            #print(self.objeto)

    def stop(self):
        self.running = False

