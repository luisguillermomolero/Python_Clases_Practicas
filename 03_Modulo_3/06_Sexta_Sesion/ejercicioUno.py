import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Clase abstracta Empleado
@dataclass
class Empleado(ABC):
    nombre: str
    salario_base: float
    
    @abstractmethod
    def calcular_salario(self):
        pass

@dataclass   
class Manager(Empleado):
    
    def calcular_salario(self):
        return self.salario_base + 5000

@dataclass
class Developer(Empleado):
    def calcular_salario(self):
        return self.salario_base + 2000
    
def calcular_total_salario(empleado: Empleado) -> float:
    #pdb.set_trace()
    return empleado.calcular_salario()

if __name__ =="__main__":
    manager = Manager("Carlos", 5000)
    developer =  Developer("Pedro", 2000)
    
    print(calcular_total_salario(manager))
    print(calcular_total_salario(developer))


