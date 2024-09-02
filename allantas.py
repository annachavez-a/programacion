# Clase base Fabrica
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_detalles(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

# Clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)

# Clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)

# Ejemplo de uso
moto = Moto(color="Rojo", precio=5000)
carro = Carro(color="Azul", precio=15000)

print("Detalles de la moto:")
moto.mostrar_detalles()

print("\nDetalles del carro:")
carro.mostrar_detalles() 

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.9  # Aplica un descuento del 10%

class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)  # Las motos siempre tienen 2 llantas

class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)  # Los carros siempre tienen 4 llantas

# Crear objetos de cada clase
moto = Moto("Rojo", 120000)
carro = Carro("Azul", 80000)

# Aplicar descuento si es necesario
moto.aplicar_descuento()
carro.aplicar_descuento()

# Mostrar los atributos de cada objeto
print("Moto:")
moto.mostrar_atributos()

print("\nCarro:")
carro.mostrar_atributos()
