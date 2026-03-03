class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo
    def getMaterial(self):
        return self.__material
    def getTipo(self):
        return self.__tipo
    def setMaterial(self, material):
        self.__material = material
    def setTipo(self, tipo):
        self.__tipo = tipo
    def __str__(self):
        return "Nombre:" + self.nombre + "\n" + \
               "Material:" + self.__material + "\n" + \
               "Tipo:" + self.__tipo

i1 = Instrumento("Saxofon", "laton", "Cuerda")
i2 = Instrumento("Flauta", "Metal", "Aire")

print(i1)
print(i2)