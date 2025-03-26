"""_summary_

    Returns:
        _type_: _description_
"""
class Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas
    
    def calcular_comision(self):
        if self.ventas > 5000:
            return self.ventas * 0.10
        return self.ventas * 0.05
    
empleados = [
    Empleado("Ana", 6000),
    Empleado("Luis", 3000),
    Empleado("Andres", 5000),
    Empleado("Juan", 10000),
    Empleado("Julian", 2500)
]

for emp in empleados:
    print(f"Empleado: {emp.nombre}, Comisión: {emp.calcular_comision()}")