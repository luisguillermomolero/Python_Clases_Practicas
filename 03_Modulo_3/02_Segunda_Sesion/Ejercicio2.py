# Implementar un sistema de monitoreo para facturación c/manejo de excepciones por consola y .log file

import logging
from dataclasses import dataclass

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='ejercicio2.log',
    filemode='a'
    )

# Crear un nuevo handler para gestionar mensaje de auditoria por .log y por consola
console_handler = logging.StreamHandler() # crear una instancia, es decir, un nuevo manejador
console_handler.setLevel(logging.DEBUG) # Configurar el nivel del logging, en este caso, el nivel mas leve
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',)) # Dando formato de salida al logging
logging.getLogger().addHandler(console_handler) # Agregando la instancia console_handler al manejador principal

@dataclass
class Factura:
    cliente: str
    cantidad: int
    precio_unitario: float
    
    def procesar(self):
        try:
            logging.info(f"Iniciando el processo de facturacion para el cliente {self.cliente}")
            
            if self.cantidad <= 0:
                raise ValueError(f"La cantidad del producto debe ser mayor a cero")
            if self.precio_unitario <= 0:
                raise ValueError(f"El precio debe ser mayor a cero")
            
            total = self.cantidad * self.precio_unitario
            logging.info(f"Factura fue procesada con exito. Total de la compra ${total} - Cliente: {self.cliente}")
        
        except ValueError as e:
            logging.error(f"Error de validación del cliente {self.cliente}: {e}")
        except Exception as e:
            logging.critical(f"Error inesperado al momento de procesar la factura de {self.cliente}: {e}")
        finally:
            logging.info(f"El proceso de facturacion para {self.cliente} finalizo")

if __name__ == "__main__":
    factura1 = Factura("Carlos", 10, 1500.25)
    factura1.procesar()
    
    #factura2 = Factura("Pedro", 5, 150)
    #factura2.procesar()
    
    