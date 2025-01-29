# Uso de Breakpoint simples
class Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas
    
    def calculo_comision(self):
        
        if self.ventas > 5000:
            print(f"***** Empleado: {self.nombre}. Ventas:{self.ventas}. Comisión del 10%")
            return self.ventas * 0.10
        
        
        print(f"***** Empleado: {self.nombre}. Ventas:{self.ventas}. Comisión del 5%")
        return self.ventas * 0.05
    
empleados = [
    Empleado("Ana", 6000),
    Empleado("Luis", 3000)
]

for emp in empleados:
    print(f"Empleado: {emp.nombre}. Comisión: {emp.calculo_comision()}")

        