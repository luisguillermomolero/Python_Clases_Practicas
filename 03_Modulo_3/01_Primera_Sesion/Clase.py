# App que permita dividir dos números
"""
# Con captura de excepciones

def division_cero(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
    except ZeroDivisionError as e:
        print("La división entre Cero no se puede lograr")
        return None

division_cero(2,0)

# Sin captura de excepciones

def division_cero(numero1, numero2):
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
division_cero(2,0)

# Mismo ejercicio explicando las excepciones múltiples

def division_segura():
    try:
        numerador = int(input("Ingrese por favor el numerador de la división: "))
        denominador = int(input("Ingrese por favor el denominador de la división: "))
        resultado =  numerador / denominador
        print(f"El resultado de la división de {numerador} entre el {denominador} es igual a: {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error {e}")

division_segura()


# Manejo de excepciones específicas "Exception" << No es recomendable SIEMPRE ya que puede esconder errores >>

def abrir_archivo():
    try:
        with open("datos.txt", "r") as archivo:
            contenido =  archivo.read()
            numero = int(contenido.strip())
            print(numero)
    except Exception as e:
        print(f"Se produjo un error{e}")

abrir_archivo()


# Uso del else y finally

# Ejercicio de división por Cero

def division_completa():
    try:
        numero = int(input("Ingrese un número: "))
        resultado = 10 / numero
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print(f"El resultado de la división es {resultado}")
    finally:
        print("La operación finalizo...")

division_completa()

"""

# App que permite procesar pedidos
# Validar que el código de producto zea alfanumerico
# Validar que la canitidad zea mayor a Cero

def procesar_pedido():
    try:
        codigo_producto = input("Ingreze el código del producto: ")
        cantidad = int(input("Ingreze la cantidad del producto: "))
        
        # Validar que el código de producto zea alfanumerico
        if not codigo_producto.isalnum():
            raise ValueError("El código del producto debe er alfanumerico")
        
        # Validar que la cantidad zea mayor a Cero
        if cantidad <= 0:
            raise ValueError("La cantidad del producto debe ser mayor a Cero")
        
        precio_unitario = 50
        total = precio_unitario * cantidad
    
    except ValueError as e:
        print(f"Error al procezar el pedido: {e}")
    else:
        print(f"Total a pagar: {total}")
    finally:
        print("Operación finalizada")

procesar_pedido()