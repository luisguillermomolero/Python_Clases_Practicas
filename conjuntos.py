# Conjuntos (set) en Python
# App de gestion de clientes (únicos) de una campaña de mercadeo

from typing import Set

def obtener_clientes_unicos(clientes: Set[str], nuevos_clientes: Set[str]) -> Set[str]:
    return clientes.union(nuevos_clientes)

def gestionar_clientes(clientes: Set[str]) -> None:
    
    # Agregar un cliente
    clientes.add("Pedro")
    print("Clientes después de agregar a Pedro: ", clientes)
    
    # Agregar un cliente duplicado
    clientes.add("Carlos")
    print("Clientes después de intentar agregar a Carlos: ", clientes)
    
    # Uso de la función remove para eliminar un cliente (si existe, y si no => ERROR)
    cliente = "Ana"
    clientes.remove(cliente)
    print("Clientes despues de eliminar a Ana con el método remove: ", clientes)
    
    # Uso de la función discard para eliminar un elemento del Set
    cliente2 = "Luis"
    clientes.discard(cliente2)
    print("Clientes después de eliminar a Luis con el método Discard: ", clientes)
    
    # Uso del método POP para mostrar un elemento del Set y posterior lo borra automaticamente
    cliente_removido = clientes.pop()
    print(f"Cliente removido aleatoriamente: {cliente_removido}")
    print("Clientes restantes:", clientes)
    
    # Borrar todos los elementos del Set
    clientes.clear()
    print("Clientes después del método Clear: ", clientes)
    
def main():
    
    clientes_antiguos = {"Carlos", "Ana", "Luis"}
    clientes_nuevos = {"Luis", "Mária", "Jorge"}
    clientes_finales = obtener_clientes_unicos(clientes_antiguos, clientes_nuevos)
    print("La lista actualizada de clientes es: ", clientes_finales)
    
    gestionar_clientes(clientes_finales)

if __name__ == "__main__":
    main()