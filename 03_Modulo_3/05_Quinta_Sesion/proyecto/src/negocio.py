from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vendedor(ABC):
    """_summary_
            Implementación de clase abstracta para definir la clase "Vendedor"
    Args:
        ABC (_type_): _description_
        nombre str
        ventas float
    """
    nombre: str
    ventas: float
    
    @abstractmethod
    def calcular_comision(self) -> float:
        """bloque de código"""
        pass

@dataclass
class VendedorBase(Vendedor):
    """
        Implementación concreta de un vendedor con una comisión por venta del 10%
    """
    def calcular_comision(self) -> float:
        return self.ventas * 0.10
    
@dataclass
class VendedorPremium(Vendedor):
    """
        Implementación concreta de un vendedor con una comisión por venta de 15%
    """
    
    def calcular_comision(self):
        return self.ventas * 0.15