class Televisor:
    def __init__(self, marca, resolucion, tipo):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo
    def getMarca(self):
        return self.__marca
    def getResolucion(self):
        return self.__resolucion
    def getTipo(self):
        return self.__tipo
    def __str__(self):
        return "Marca:" + self.__marca + "\n" + \
               "Resolucion:" + str(self.__resolucion) + "\n" + \
               "Tipo:" + self.__tipo

t1 = Televisor("Samsung", 1080, "LED")
t2 = Televisor("LG", 2160, "OLED")

print(t1)
print(t2)