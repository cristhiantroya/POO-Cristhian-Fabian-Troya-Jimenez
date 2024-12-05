# Definimos una clase base llamada Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        """
        Constructor de la clase Vehiculo.

        :param marca: Marca del vehículo.
        :param modelo: Modelo del vehículo.
        :param año: Año de fabricación del vehículo.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        """Método para describir el vehículo."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

    def arrancar(self):
        """Método genérico para arrancar el vehículo."""
        print("El vehículo está arrancando")

    def detener(self):
        """Método genérico para detener el vehículo."""
        print("El vehículo se ha detenido")


# Definimos una clase derivada llamada Carro que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        """
        Constructor de la clase Carro.

        :param marca: Marca del carro.
        :param modelo: Modelo del carro.
        :param año: Año de fabricación del carro.
        :param puertas: Número de puertas del carro.
        """
        super().__init__(marca, modelo, año)

        # Validación para asegurarse de que el número de puertas sea válido
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que 0.")

        self.puertas = puertas

    def describir(self):
        """Sobrescribimos el método describir para incluir el número de puertas."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Puertas: {self.puertas}")

    def arrancar(self):
        """Sobrescribimos el método arrancar para Carro."""
        print("El carro está arrancando")


# Definimos otra clase derivada llamada Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        """
        Constructor de la clase Motocicleta.

        :param marca: Marca de la motocicleta.
        :param modelo: Modelo de la motocicleta.
        :param año: Año de fabricación de la motocicleta.
        :param tipo: Tipo de motocicleta (e.g., deportiva, cruiser).
        """
        super().__init__(marca, modelo, año)

        # Validación para asegurarse de que el tipo no esté vacío
        if not tipo:
            raise ValueError("El tipo de motocicleta no puede estar vacío.")

        self.tipo = tipo

    def describir(self):
        """Sobrescribimos el método describir para incluir el tipo de motocicleta."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Tipo: {self.tipo}")

    def arrancar(self):
        """Sobrescribimos el método arrancar para Motocicleta."""
        print("La motocicleta está arrancando")


# Creamos instancias de Carro y Motocicleta
try:
    mi_carro = Carro("Toyota", "Corolla", 2020, 4)
    mi_motocicleta = Motocicleta("Yamaha", "MT-07", 2021, "Deportiva")

    # Llamamos a los métodos de las instancias
    mi_carro.arrancar()  # Salida: El carro está arrancando
    mi_carro.describir()  # Salida: Marca: Toyota, Modelo: Corolla, Año: 2020, Puertas: 4
    mi_carro.detener()  # Salida: El vehículo se ha detenido

    mi_motocicleta.arrancar()  # Salida: La motocicleta está arrancando
    mi_motocicleta.describir()  # Salida: Marca: Yamaha, Modelo: MT-07, Año: 2021, Tipo: Deportiva
    mi_motocicleta.detener()  # Salida: El vehículo se ha detenido

except ValueError as e:
    print(f"Error al crear el vehículo: {e}")

