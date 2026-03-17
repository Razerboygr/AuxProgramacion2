from multimethod import multimethod
class Jugador:
    def __init__(self, nombre="", diamantes=0):
        self.nombre = nombre
        self.diamantes = diamantes
    def __str__(self):
        return f"{self.nombre} : {self.diamantes} diamantes"
    @multimethod
    def stacks(self, x:bool):
        return self.diamantes // 64
    @multimethod
    def stacks(self, extra:int):
        return (self.diamantes + extra) // 64

class ServidorMinecraft:
    def __init__(self):
        self.jugadores = []
    @multimethod
    def agregar(self, j:Jugador):
        if len(self.jugadores) < 10:
            self.jugadores.append(j)
    @multimethod
    def agregar(self, nombre:str, diamantes:int):
        if len(self.jugadores) < 10:
            self.jugadores.append(Jugador(nombre, diamantes))
    @multimethod
    def mostrar(self, x:bool):
        for j in self.jugadores:
            print(j.nombre, "tiene", j.stacks(True), "stacks")
    @multimethod
    def mostrar(self, extra:int):
        for j in self.jugadores:
            print(j.nombre, "tendria", j.stacks(extra), "stacks")
    def masDiam(self):
        mayor = self.jugadores[0]
        for j in self.jugadores:
            if j.diamantes > mayor.diamantes:
                mayor = j
        return mayor.nombre
    def total(self):
        suma = 0
        for j in self.jugadores:
            suma += j.diamantes
        return suma

class Main():
    s = ServidorMinecraft()
    s.agregar(Jugador("Steve",120))
    s.agregar("Alex",80)
    s.agregar("Juan",30)
    s.mostrar(True)
    s.mostrar(20)
    print("Jugador con mas diamantes:", s.masDiam())
    print("Total diamantes:", s.total())