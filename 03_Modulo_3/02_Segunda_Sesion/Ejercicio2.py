import logging
from dataclasses import dataclass, field

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='eventos.log',
                    filemode='a')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

@dataclass
class Producto:
    nombre: str
    precio: int
    cantidad: int
    
    def comprar(self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error(f"Error: No hay suficiente stock de '{self.nombre}'. Stock disponible: {self.cantidad}")
            raise ValueError(f"No hay suficiente stock de '{self.nombre}'. Solo quedan {self.cantidad} unidades")
        else:
            self.cantidad -= cantidad
            logging.info(f"Compra exitosa: {cantidad} unidades de '{self.nombre}'. Stock restante {self.cantidad} unidades")
            return self.precio * cantidad

@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        logging.debug(f"Producto agregado: {producto.nombre} - Precio: {producto.precio} - Stock: {producto.cantidad}")
    
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            try:
                total = producto.comprar(cantidad)
                logging.info(f"Compra realizada: {cantidad} unidades de '{nombre_producto}' por un total de ${total}")
                return total
            except ValueError as e:
                logging.error(f"Error en la compra: {e}")
        
        else:
            logging.warning(f"Producto no registrado en el Stock {nombre_producto}")

if __name__ == "__main__":
    tienda = Tienda()
    
    inventario_portatil = Producto(nombre="Laptop", precio=1000, cantidad=5)
    inventario_teclado = Producto(nombre="Teclado", precio=50, cantidad=20)
    tienda.agregar_producto(inventario_portatil)
    tienda.agregar_producto(inventario_teclado)
    
    tienda.realizar_compra("Laptop", 1)
    tienda.realizar_compra("Teclado", 2)
    
    # Casos de pruebas participantes/clase
    tienda.realizar_compra("Laptop", 10) #False
    tienda.realizar_compra("Mouse", 5) #False
    tienda.realizar_compra("TECLADO", 32) #False
    tienda.realizar_compra("teclado", 2) #False
    tienda.realizar_compra("Procesadores", 4) #False
    tienda.realizar_compra("Monitores", 2) #False
    tienda.realizar_compra(42, "Siete") #False
    
    
    
    
    
    
            
        
            
    

