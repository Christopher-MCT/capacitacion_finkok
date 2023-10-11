

class Animal:
    def __init__(self, nombre, edad, patas):
        self.nombre = nombre
        self.edad = edad
        self.patas = patas
        
    def describe_me(self):
        print(f"Tengo {self.patas} patas")
        print(f"Me llamo {self.nombre} y tengo {self.edad} años ")
        