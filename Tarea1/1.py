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


# Prueba
obj1 = Anime("Naruto", "Shonen", 220)
obj2 = Anime("Death Note", "Suspenso", 37)

obj1.agregarEpisodio("Episodio 15")
obj2.agregarEpisodio("Episodio 34")

print(obj1)
print(obj2)