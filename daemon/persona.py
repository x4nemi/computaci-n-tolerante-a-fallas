
class Persona:
    def __init__(self, nombre = '', edad = None):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Persona\nNombre: {self.nombre}   Edad: {str(self.edad)}\n\n'
    
    def recuperar(self):
        with open('persona.txt', 'r') as file:
            self.nombre = file.readline().strip()
            self.edad = int(file.readline())