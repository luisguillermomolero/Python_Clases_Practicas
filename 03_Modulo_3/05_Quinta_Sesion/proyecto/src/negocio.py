from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vendedor(ABC):
    nombre: str
    ventas: float
    
    @abstractmethod
    def calcular_comision(self) -> float:
        pass

@dataclass
class VendedorBase(Vendedor):
    
    def calcular_comision(self) -> float:
        return self.ventas * 0.10

@dataclass
class VendedorPremium(Vendedor):
    
    def calcular_comision(self) -> float:
        return self.ventas * 0.15

