# App: Gestión de pedidos de una tienda
def agregar_pedido(pedidos: list[str], nuevo_pedido: str) -> list[str]:
    pedidos.append(nuevo_pedido)
    return pedidos

def eliminar_pedido(pedidos: list[str], pedido_a_eliminar: str) -> list[str]:
    if pedido_a_eliminar in pedidos:
        pedidos.remove(pedido_a_eliminar)
    else:
        print("El pedido no se encuentra en la lista")
    return pedidos

def buscar_pedido(pedidos: list[str], pedido_a_buscar: str) -> int:
    if pedido_a_buscar in pedidos:
        return pedidos.index(pedido_a_buscar)
    else:
        print("El pedido no se encuentra en la lista")
        return -1

def main():
    # Lista inicial de pedidos
    pedidos_tienda = ["Pedido 1", "Pedido 3"]
    
    # Agregar un nuevo pedido a la lista
    pedidos_tienda = agregar_pedido(pedidos_tienda, "Pedido 2")
    
    # Mostrar los elementos de la lista de forma desordenada
    print("Lista actualizada de pedidos", pedidos_tienda)
    
    # Ordene la lista
    pedidos_tienda.sort()
    print("Lista actualizada de pedidos ordenadas", pedidos_tienda)
    
    # Buscar un pedido en específico
    pedido_a_buscar = "Pedido 3"
    indice = buscar_pedido(pedidos_tienda, pedido_a_buscar)
    if indice != -1:
        print(f"El {pedido_a_buscar} se encuentra en la posición {indice}")
    
    # Eliminar un pedido de la lista
    pedido_a_eliminar = "Pedido 1"
    pedidos_tienda = eliminar_pedido(pedidos_tienda, pedido_a_eliminar)
    print(f"La lista resultante luego de eliminar el {pedido_a_eliminar} es {pedidos_tienda}")

if __name__ == "__main__":
    main()
