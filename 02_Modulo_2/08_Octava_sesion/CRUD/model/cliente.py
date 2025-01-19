from .persona import Persona

class Cliente(Persona):
    """Clase que representa a un cliente, hereda de Persona."""

    def __init__(self, nombre, telefono, direccion):
        super().__init__(nombre, telefono, direccion)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_info(self):
        print(f"Cliente: {self._nombre}, Teléfono: {self._telefono}, Dirección: {self._direccion}")
