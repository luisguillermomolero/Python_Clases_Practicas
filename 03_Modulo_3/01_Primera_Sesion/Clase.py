"""
# Excepciones

def division_segura(numero1, numero2):
    try:
        resultado = numero1/numero2
        print("El resultado de la división es: ", resultado)
    except ZeroDivisionError:
        print("No es posible desarrollar esta división")
        return None

division_segura(10, 0)

# Manejo avanzado de excepciones

def division_segura_dos():
    try:
        numerador = int(input("Ingrese el numerador: "))
        denominador = int(input("Ingrese el denominador: "))
        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error:  {e}")

division_segura_dos()


try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        numero = int(contenido.strip())
        resultado = 100 / numero
        print(f"El resultado es: {resultado}")
except Exception as e:
    print(f"Se genero un ERROR: {e}")



# try, except, else, finally

try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Error: Entrada invalida. {e}")
except ZeroDivisionError as e:
    print(f"Error: No se puede desarrollar una división entre cero:")
else:
    print(f"El resultad es: {resultado}")
finally:
    print("Ejercicio finalizado")
    


def procesar_pedido(codigo_producto, cantidad):
    try:
        # Simular una validación de datos
        if not codigo_producto.isalnum():
            # raise ERROR: gestiona de forma manual y en tiempo de ejecucuión un ERROR
            raise ValueError("El código del producto debe ser alfanúmerico")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser superior a cero")
        
        # Simular el calculo del total
        precio_unitario = 100 # ejemplo del precio por unidad
        total = precio_unitario * cantidad
    
    except ValueError as e:
        print(f"Error al procesar el pedido: {e}")
    else:
        print(f"Pedido procesado exitosamente. El total a pagar es: ${total:.2f}")
    finally:
        print("Operación finalizada. Registro actualizado")

# método principal

if __name__ == "__main__":
    procesar_pedido("ABC123", 2)
    procesar_pedido("######", 12)
    procesar_pedido("GHJ8547", -10)
    procesar_pedido("GHJ8547", 10.25)
    
"""

class ErrorDePago(Exception):
    pass

class PasarelaDePago:
    @staticmethod
    def procesar_pago(numero_tarjeta, monto):
        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("El número de la tarjeta no es valido. Debe iniciar en 4")
        if monto <= 0:
            raise ErrorDePago("El monto de la compra debe ser superior a cero")
        if len(numero_tarjeta) != 16:
            raise ErrorDePago("El número de la tarjeta debe tener 16 digitos")
        
        return f"El pago de ${monto} fue procesado con éxito."

def proceso_pago_cliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f"Iniciando el proceso de pago de {nombre_cliente}...")
        resultado = PasarelaDePago.procesar_pago(numero_tarjeta, monto)
    except ErrorDePago as e:
        print(f"Error al procesar el pago: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    else:
        print(resultado)
    finally:
        print("El registro de la transacción finalizo.")

if __name__ == "__main__":
    #proceso_pago_cliente("Luis Molero", "4111111111111111", 456.52)
    #proceso_pago_cliente("Andrés Serrano", "5111111111111111", 80.23)
    proceso_pago_cliente("Alfonso Cantillo", "4123541256327458", -250)
    