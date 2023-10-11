from clase2_a import Animal


class Perro(Animal):
    def __init__(self, nombre, edad, patas, duenio):
        super(Perro, self).__init__(nombre, edad, patas)
        self.duenio = duenio
        
    def describe_me(self):
        super(Perro, self).describe_me()
        print(f"El dueño es {self.duenio} ")
        
dog = Perro("Pasicuato", 7, 4, "MrData")
dog.describe_me()