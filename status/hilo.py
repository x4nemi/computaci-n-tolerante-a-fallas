import pickle
from threading import Thread

# Clase para el hilo
# Se va a correr mientras se esté guardando, muchas veces
class SerializarHilo(Thread):
    def __init__(self, objeto):
        Thread.__init__(self)
        self.running = True
        self.objeto = objeto
        self.daemon = True

    def run(self):
        while self.running:
            try:
                fileHander = open("paqueterias", "wb")
                pickle.dump(self.objeto, fileHander)
            except:
                print("No se pudo guardad")
            finally:
                fileHander.close()

    def stop(self):
        self.running = False

