from clase1_a import Animal


class Gato(Animal):
    def araniar(self):
        print("te añaño")
        
        
cat = Gato("Mazapan", 2, 4) 
cat.describe_me()
print(cat.nombre)

cat.araniar()
 
#dog = Gato("Milaneso", 5, 4)

#dog.describe_me()
#print(dog.nombre)
#print(dog.patas)