from model.cliente import Cliente
from model.mascota import Mascota
from model.cita import Cita
from utils.validaciones import validar_telefono, validar_fecha, validar_hora

class MenuController:
    """Controlador principal para gestionar las opciones del menú"""

    def __init__(self):
        """Inicializa el controlador con una lista de clientes vacía."""
        self.clientes = []  # Lista de clientes para este controlador

    def registrar_cliente(self):
        print("\n--- Registrar Cliente ---")
        nombre = input("Nombre del cliente: ")
        telefono = input("Teléfono del cliente: ")
        while not validar_telefono(telefono):
            print("Número de teléfono inválido. Intente nuevamente.")
            telefono = input("Teléfono del cliente: ")
        direccion = input("Dirección del cliente: ")
        cliente = Cliente(nombre, telefono, direccion)
        self.clientes.append(cliente)  # Agregar el cliente a la lista
        print(f"\nCliente {nombre} registrado exitosamente.")

    def registrar_mascota(self):
        print("\n--- Registrar Mascota ---")
        if not self.clientes:
            print("No hay clientes registrados. Primero registre un cliente.")
            return

        nombre_cliente = input("Nombre del cliente propietario: ")
        cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)

        if cliente:
            nombre_mascota = input("Nombre de la mascota: ")
            especie = input("Especie de la mascota: ")
            raza = input("Raza de la mascota: ")
            edad = input("Edad de la mascota: ")
            mascota = Mascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print(f"Mascota {nombre_mascota} registrada para el cliente {nombre_cliente}.")
        else:
            print("Cliente no encontrado.")

    def programar_cita(self):
        print("\n--- Programar Cita ---")
        if not self.clientes:
            print("No hay clientes registrados. Primero registre un cliente.")
            return

        nombre_cliente = input("Nombre del cliente propietario: ")
        cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)

        if cliente:
            nombre_mascota = input("Nombre de la mascota: ")
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)

            if mascota:
                fecha = input("Fecha de la cita (YYYY-MM-DD): ")
                while not validar_fecha(fecha):
                    print("Fecha inválida. Formato correcto: YYYY-MM-DD")
                    fecha = input("Fecha de la cita (YYYY-MM-DD): ")

                hora = input("Hora de la cita (HH:MM): ")
                while not validar_hora(hora):
                    print("Hora inválida. Formato correcto: HH:MM")
                    hora = input("Hora de la cita (HH:MM): ")

                servicio = input("Servicio (consulta, vacunación, etc.): ")
                veterinario = input("Veterinario asignado: ")
                cita = Cita(fecha, hora, servicio, veterinario)
                mascota.agregar_cita(cita)
                print(f"Cita programada para {mascota.nombre} el {fecha} a las {hora}.")
            else:
                print("Mascota no encontrada.")
        else:
            print("Cliente no encontrado.")

    def consultar_historial(self):
        print("\n--- Consultar Historial de Mascotas ---")
        if not self.clientes:
            print("No hay clientes registrados. Primero registre un cliente.")
            return

        nombre_cliente = input("Nombre del cliente propietario: ")
        cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)

        if cliente:
            nombre_mascota = input("Nombre de la mascota: ")
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)

            if mascota:
                print("\nHistorial de Citas y Servicios para:", mascota.nombre)
                print("-" * 50)
                print("Citas programadas:")
                for cita in mascota.historial_citas:
                    cita.mostrar_info()
                print("-" * 50)
                print("Servicios realizados:")
                for servicio in mascota.historial_servicios:
                    print(f"- {servicio}")
                print("-" * 50)
            else:
                print("Mascota no encontrada.")
        else:
            print("Cliente no encontrado.")

    def gestionar_citas(self):
        print("\n--- Gestionar Citas ---")
        # Aquí puedes implementar opciones para gestionar las citas de una mascota
        pass
