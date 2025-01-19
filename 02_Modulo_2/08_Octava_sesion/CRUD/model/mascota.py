class Mascota:
    """Clase que representa a una mascota."""

    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = []
        self.historial_servicios = []

    def agregar_cita(self, cita):
        self.historial_citas.append(cita)

    def agregar_servicio(self, servicio):
        self.historial_servicios.append(servicio)
