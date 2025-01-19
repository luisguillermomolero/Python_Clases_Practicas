class Cita:
    """Clase que representa una cita médica."""

    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario

    def mostrar_info(self):
        print(f"Cita: {self.fecha} {self.hora} - {self.servicio} con {self.veterinario}")
