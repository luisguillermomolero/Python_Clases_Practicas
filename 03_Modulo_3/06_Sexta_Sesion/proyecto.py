import logging
import pdb
from dataclasses import dataclass
from datetime import date

# Configuración básica de logging
logging.basicConfig(level=logging.DEBUG)

# Clase Cliente
@dataclass
class Cliente:
    nombre: str
    documento_identidad: str

    def __str__(self):
        return f"{self.nombre} (ID: {self.documento_identidad})"

# Clase Habitacion
@dataclass
class Habitacion:
    numero: int
    tipo: str  # Ejemplo: "individual", "doble", etc.
    precio_noche: float

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio_noche} por noche"

# Clase Reserva
@dataclass
class Reserva:
    cliente: Cliente
    habitacion: Habitacion
    fecha_entrada: date
    fecha_salida: date

    def calcular_total(self) -> float:
        """Calcula el total de la reserva en función de las fechas de entrada y salida"""
        noches = (self.fecha_salida - self.fecha_entrada).days
        total = noches * self.habitacion.precio_noche
        logging.debug(f"Total por {noches} noches en {self.habitacion.tipo}: ${total}")
        return total

    def mostrar_detalles(self):
        """Muestra los detalles de la reserva"""
        logging.debug(f"Detalles de la reserva:")
        logging.debug(f"Cliente: {self.cliente}")
        logging.debug(f"Habitación: {self.habitacion}")
        logging.debug(f"Fechas: {self.fecha_entrada} - {self.fecha_salida}")
        logging.debug(f"Total: ${self.calcular_total()}")

# Función principal
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", "12345678")

    # Crear habitaciones
    habitacion1 = Habitacion(101, "individual", 100)
    habitacion2 = Habitacion(102, "doble", 150)

    # Crear una reserva
    reserva1 = Reserva(cliente1, habitacion1, date(2025, 2, 1), date(2025, 2, 5))

    # Depuración con pdb
    pdb.set_trace()  # Aquí se interrumpe la ejecución y entra en modo pdb para depurar

    # Mostrar detalles de la reserva
    reserva1.mostrar_detalles()
