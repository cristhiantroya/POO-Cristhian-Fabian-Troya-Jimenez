class Empleado:
    def __init__(self, nombre, dni):
        """
        Constructor de la clase Empleado.

        :param nombre: Nombre del empleado.
        :param dni: Documento Nacional de Identidad del empleado.
        """
        self.nombre = nombre
        self.dni = dni

    def calcular_salario(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        Este método será sobrescrito en las clases derivadas.
        """
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

    def mostrar_informacion(self):
        """Muestra información básica del empleado."""
        print(f"Nombre: {self.nombre}, DNI: {self.dni}")


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, dni, horas_trabajadas, tarifa_por_hora):
        """
        Constructor de la clase EmpleadoPorHora.

        :param nombre: Nombre del empleado.
        :param dni: Documento Nacional de Identidad del empleado.
        :param horas_trabajadas: Número de horas trabajadas en el mes.
        :param tarifa_por_hora: Tarifa por hora trabajada.
        """
        super().__init__(nombre, dni)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        """Calcula el salario del empleado por hora."""
        return self.horas_trabajadas * self.tarifa_por_hora


class EmpleadoPorSueldo(Empleado):
    def __init__(self, nombre, dni, sueldo_mensual):
        """
        Constructor de la clase EmpleadoPorSueldo.

        :param nombre: Nombre del empleado.
        :param dni: Documento Nacional de Identidad del empleado.
        :param sueldo_mensual: Sueldo mensual del empleado.
        """
        super().__init__(nombre, dni)
        self.sueldo_mensual = sueldo_mensual

    def calcular_salario(self):
        """Devuelve el sueldo mensual del empleado."""
        return self.sueldo_mensual


# Función para mostrar la información y salario de un empleado
def mostrar_informacion_empleado(empleado):
    """
    Muestra la información y el salario del empleado.

    :param empleado: Objeto de tipo Empleado (o sus derivados).
    """
    empleado.mostrar_informacion()
    print(f"Salario: {empleado.calcular_salario()}\n")


# Crear instancias de empleados
empleado1 = EmpleadoPorHora("Juan Pérez", "12345678A", 160, 15)  # 160 horas trabajadas a 15 por hora
empleado2 = EmpleadoPorSueldo("Ana Gómez", "87654321B", 2000)      # Sueldo mensual de 2000

# Mostrar información y salarios
mostrar_informacion_empleado(empleado1)
mostrar_informacion_empleado(empleado2)