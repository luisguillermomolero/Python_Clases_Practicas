import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

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

class Developer(Empleado):
    def calcular_salario(self):
        return self.salario_base + 2000

def calcular_total_salario(empleado: Empleado) -> float:
    """_summary_
    
    n = Avance de linea en linea
    s = Para saltar de funcion (método) en función (método)
    c = Para saltar hacia la siguiente pausa
    p variable = Muestra el valor de una variable en algún momento de la ejecucuión

    """
    pdb.set_trace() # activación del debuger
    return empleado.calcular_salario()

if __name__ == '__main__':
    manager = Manager("Pascual", 30000)
    developer = Developer("Jacinta", 25000)
    
    print(calcular_total_salario(manager))
    print(calcular_total_salario(developer))

