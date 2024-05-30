from random import*

nombre = 0
nombre = randint(0, 100)

while True:
    nombre_choisis = int(input("entrez le nombre que vous avez choisis"))
    if nombre_choisis>nombre:
      print("le nombre est trop grand réessayez")
    if nombre_choisis<nombre:
      print("le nombre est trop petit")
    if nombre_choisis == nombre:
        print("vous avez gagné !")
