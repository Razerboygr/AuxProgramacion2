class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes
    def stacksDiamantes(self):
        return self.diamantes // 64
    
class ServidorMinecraft:
    def __init__(self):
        self.jugadores = []
    def agregarJugador(self, j):
        if len(self.jugadores) < 10:
            self.jugadores.append(j)
    def mostrarStacks(self):
        for j in self.jugadores:
            print(j.nombre, "tiene", j.stacksDiamantes(), "stacks de diamantes")
    def jugadorMasDiamantes(self):
        mayor = self.jugadores[0]
        for j in self.jugadores:
            if j.diamantes > mayor.diamantes:
                mayor = j
        return mayor.nombre
    def totalDiamantes(self):
        suma = 0
        for j in self.jugadores:
            suma += j.diamantes
        return suma


class Main():
    s = ServidorMinecraft()
    s.agregarJugador(Jugador("Steve", 120))
    s.agregarJugador(Jugador("Alex", 80))
    s.agregarJugador(Jugador("Juan", 30))
    s.mostrarStacks()
    print("Jugador con mas diamantes:", s.jugadorMasDiamantes())
    print("Total diamantes:", s.totalDiamantes())