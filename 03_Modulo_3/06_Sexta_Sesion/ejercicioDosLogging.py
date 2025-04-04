import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)


@dataclass
class Vendedor:
    nombre: str
    ventas_totales: float
    
    def calculo_comision(self) -> float:
        if self.ventas_totales > 10000:
            comision = self.ventas_totales * 0.10
            logging.debug(f"{self.nombre} ha alcanzado el umbral de vetnas. Comision de {comision}")
        else:
            comision = self.ventas_totales * 0.05
            logging.debug(f"{self.nombre} ha alcanzado el umbral de vetnas. Comision de {comision}")

if __name__ == "__main__":
    vendedor = Vendedor("Carol", 20000)
    vendedorDos = Vendedor("Juan", 5000)
    