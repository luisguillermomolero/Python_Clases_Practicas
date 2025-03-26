"""_summary_
"""
class Reserva:
    def __init__(self, cliente, fecha = None):
        self.cliente = cliente
        self.fecha = fecha if fecha is not None else "Fecha no asiganada"
    
reservas = [
    Reserva("Juan"),
    Reserva("Ana", "2025-03-25")
]

for reserva in reservas:
    if reserva.fecha == "Fecha no asiganada":
        print(f"ERROR: Fecha de reserva no asignada para el cliente {reserva.cliente}")
    else:
        print(f"La reserva de {reserva.cliente} es para la fecha: {reserva.fecha}")