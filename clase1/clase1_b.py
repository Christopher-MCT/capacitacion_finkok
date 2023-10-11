from clase1_a import Animal


class Perro(Animal):
     pass
 
 
dog = Perro("Chucito", 5, 4)

dog.describe_me()
print(dog.nombre)
print(dog.patas)