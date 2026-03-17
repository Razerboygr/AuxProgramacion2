from multimethod import multimethod

class Bus:
    def __init__(self, capacidad):
        self.cap = capacidad
        self.pas = 0
        self.pasaje = 1.50
    def __str__(self):
        return f"Bus: {self.pas} pasajeros"
    @multimethod
    def subir(self, x:int):
        if self.pas + x <= self.cap:
            self.pas += x
        else:
            print("No hay asientos")
    @multimethod
    def subir(self, x:int, y:int):
        total = x + y
        if self.pas + total <= self.cap:
            self.pas += total
        else:
            print("No hay asientos")
    @multimethod
    def cobrar(self, x:bool):
        return self.pas * self.pasaje
    @multimethod
    def cobrar(self, desc:float):
        return (self.pas * self.pasaje) * (1-desc)
    def libres(self):
        return self.cap - self.pas

class Main():
    b = Bus(40)
    b.subir(20)
    b.subir(3,2)
    print("Pasajeros:", b.pas)
    print("Total:", b.cobrar(True))
    print("Total con descuento:", b.cobrar(0.20))
    print("Asientos libres:", b.libres())