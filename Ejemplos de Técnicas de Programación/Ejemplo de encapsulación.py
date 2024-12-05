class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase CuentaBancaria.

        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto es 0).
        """
        self.titular = titular  # Nombre del titular de la cuenta
        self.__saldo = saldo_inicial  # Saldo privado de la cuenta, se inicia con el saldo inicial

    def depositar(self, cantidad):
        """
        Método para depositar dinero en la cuenta.

        :param cantidad: Monto a depositar.
        """
        if cantidad > 0:  # Verifica que la cantidad a depositar sea positiva
            self.__saldo += cantidad  # Aumenta el saldo con la cantidad depositada
            print(f"Depósito exitoso: {cantidad}. Nuevo saldo: {self.__saldo}.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta.

        :param cantidad: Monto a retirar.
        """
        if 0 < cantidad <= self.__saldo:  # Verifica que la cantidad a retirar sea positiva y no exceda el saldo
            self.__saldo -= cantidad  # Disminuye el saldo con la cantidad retirada
            print(f"Retiro exitoso: {cantidad}. Nuevo saldo: {self.__saldo}.")
        else:
            print("Retiro fallido: Verifique que la cantidad sea válida.")

    def obtener_saldo(self):
        """
        Método para obtener el saldo actual de la cuenta.

        :return: Saldo actual de la cuenta.
        """
        return self.__saldo  # Retorna el saldo privado


# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)

# Imprimir el saldo inicial
print(f"Saldo inicial de {cuenta.titular}: {cuenta.obtener_saldo()}")

# Realizar algunas operaciones
cuenta.depositar(500)  # Depositar dinero
cuenta.retirar(200)  # Retirar dinero
cuenta.retirar(1500)  # Intentar retirar más de lo que hay en la cuenta

# Imprimir el saldo final
print(f"Saldo final de {cuenta.titular}: {cuenta.obtener_saldo()}")