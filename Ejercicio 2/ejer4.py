class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.pasaje = 1.50
    def subirPasajeros(self, x):
        if self.pasajeros + x <= self.capacidad:
            self.pasajeros += x
        else:
            print("No hay suficientes asientos")
    def cobrarPasaje(self):
        return self.pasajeros * self.pasaje
    def asientosDisponibles(self):
        return self.capacidad - self.pasajeros

class Main():
    b = Bus(40)
    b.subirPasajeros(25)
    print("Pasajeros en el bus:", b.pasajeros)
    print("Total recaudado:", b.cobrarPasaje())
    print("Asientos disponibles:", b.asientosDisponibles())