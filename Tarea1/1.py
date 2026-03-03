class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []
    def getNroEpisodios(self):
        return self.__nroEpisodios
    def agregarEpisodio(self, ep):
        self.__episodios.append(ep)
    def __str__(self):
        return "Nombre:" + self.nombre + "\n" + \
               "Genero:" + self.genero + "\n" + \
               "NroEpisodios:" + str(self.__nroEpisodios) + "\n" + \
               "ListaEpisodios:" + str(self.__episodios)

obj1 = Anime("Dragon ball super","Arte marcial", 131)
obj2 = Anime("Frieren","Fantasia", 28)

obj1.agregarEpisodio("Episodio 131 (el mas god :v)")
obj2.agregarEpisodio("Episodio 1 (pipipi :,v)")

print(obj1)
print(obj2)