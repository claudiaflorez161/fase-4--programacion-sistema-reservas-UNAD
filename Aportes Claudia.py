from abc import ABC, abstractmethod
#Claudia Lorena Florez Franco

# Hice esta excepción para controlar errores de los servicios.
class ServicioError(Exception):
    pass


# Esta es la clase principal de los servicios.
# La hice abstracta.
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        # Validé que el nombre no venga vacío.
        if not nombre.strip():
            raise ServicioError("El nombre del servicio está vacío")

        # También validé que el precio sea válido.
        if precio_base <= 0:
            raise ServicioError("El precio debe ser mayor a 0")

        self._nombre = nombre
        self._precio_base = precio_base

    # Este método lo dejé abstracto porque cada servicio calcula diferente.
    @abstractmethod
    def calcular_costo(self):
        pass

    # Igual acá, cada servicio tiene una descripción distinta.
    @abstractmethod
    def descripcion(self):
        pass


# Esta clase es para las salas.
class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad, disponible=True):

        super().__init__(nombre, precio_base)

        # Validé que la capacidad sí tenga sentido.
        if capacidad <= 0:
            raise ServicioError("La capacidad no puede ser menor o igual a 0")

        self._capacidad = capacidad
        self._disponible = disponible

    # Acá hice el cálculo del costo de la sala.
    # También le puse impuesto opcional.
    def calcular_costo(self, horas=1, impuesto=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser válidas")

        # Si la sala no está disponible no deja reservar.
        if not self._disponible:
            raise ServicioError("La sala no está disponible")

        total = self._precio_base * horas

        # Si mandan impuesto lo suma.
        if impuesto > 0:
            total += total * impuesto

        return total

    def descripcion(self):
        return f"Sala para {self._capacidad} personas"


# Esta clase es para alquiler de equipos.
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo, horas_maximas):

        super().__init__(nombre, precio_base)

        self._tipo_equipo = tipo_equipo
        self._horas_maximas = horas_maximas

    # Acá hice otro cálculo diferente.
    # Este funciona con descuento opcional.
    def calcular_costo(self, horas=1, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas no son válidas")

        # Regla para que no alquilen demasiadas horas.
        if horas > self._horas_maximas:
            raise ServicioError("Se pasó del límite de horas")

        total = self._precio_base * horas

        # Si tiene descuento lo resta.
        if descuento > 0:
            total -= total * descuento

        return total

    def descripcion(self):
        return f"Alquiler de equipo tipo {self._tipo_equipo}"


# Esta clase es para asesorías.
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, especialista, tiempo_minimo):

        super().__init__(nombre, precio_base)

        self._especialista = especialista
        self._tiempo_minimo = tiempo_minimo

    # Acá validé que la asesoría tenga un tiempo mínimo.
    def calcular_costo(self, horas=1, impuesto=0):

        if horas < self._tiempo_minimo:
            raise ServicioError("La asesoría necesita más tiempo mínimo")

        total = self._precio_base * horas

        # También le dejé impuesto opcional.
        if impuesto > 0:
            total += total * impuesto

        return total

    def descripcion(self):
        return f"Asesoría con {self._especialista}"


# ==========================
# Pruebas que hice
# ==========================

try:

    sala = ReservaSala("Sala premium", 100, 20)

    equipo = AlquilerEquipo(
        "Portátil gamer",
        80,
        "Laptop",
        8
    )

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        150,
        "Ingeniero Senior",
        2
    )

    print(sala.descripcion())
    print("Costo sala:", sala.calcular_costo(3, 0.19))

    print(equipo.descripcion())
    print("Costo equipo:", equipo.calcular_costo(5, 0.10))

    print(asesoria.descripcion())
    print("Costo asesoría:", asesoria.calcular_costo(3, 0.19))

except ServicioError as error:

    print("Error:", error)