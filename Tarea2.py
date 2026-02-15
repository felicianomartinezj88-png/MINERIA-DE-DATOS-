class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Acelerando... Nueva velocidad: {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Frenando... Nueva velocidad: {self.velocidad} km/h")

    def mostrar_info(self):
        print(f"--- Info Coche ---")
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
        print(f"Color: {self.color} | Velocidad Actual: {self.velocidad} km/h")

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")
        else:
            print("Fondos insuficientes para realizar el retiro.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo actual: ${self.saldo}")

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"--- Info Rectángulo ---")
        print(f"Dimensiones: {self.ancho} x {self.alto}")
        print(f"Área: {area} | Perímetro: {perimetro}")


# Ejemplo de uso
mi_coche = Coche("Toyota", "Corolla", "Rojo")
mi_coche.acelerar(50)
mi_coche.mostrar_info()

mi_cuenta = CuentaBancaria("Juan Pérez")
mi_cuenta.depositar(1000)
mi_cuenta.retirar(400)
mi_cuenta.mostrar_saldo()

mi_rect = Rectangulo(10, 5)
mi_rect.mostrar_info()