"""
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")


try:
    numero = int(input("Por favor, ingrese un número: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Debe ingresar un número entero.")
except ZeroDivisionError:
    print("Error: Recuerde que no se puede divir por cero.")
except Exception as e:
    print(f"Error inesperado: {e}")
    

try:
    archivo = open("datos.csv", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
    archivo = None
else:
    print("El archivo fue leido con éxitos")
finally:
    if archivo:
        archivo.close()
    else:
        print("Recuerda que si el archivo no existe => no lo puedo cerrar...")



# Desarrolle un ejercicio que permite leer un dato de tipo entero y que capture error cuando otro caracter es ingresado.

class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

try:
    raise ErrorPersonalizado("Este es un ejemplo de error personalizado")
except ErrorPersonalizado as e:
    print(f"Se capturo un error: {e}")
    

import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s - %(message)s",
    handlers= [
        #logging.FileHandler("Errores.log"),
        logging.StreamHandler()
    ]
)

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error(f"Error capturado: {e}")



import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s - %(message)s",
    handlers= [
        #logging.FileHandler("Errores.log"),
        logging.StreamHandler()
    ]
)

try:
    1 / 1
except ZeroDivisionError as e:
    logging.error(f"Error capturado: {e}")
else:
    logging.info("La división fue todo un éxito")
    


import asyncio

async def tarea():
    try:
        await asyncio.sleep(1)
        raise ValueError("Error en tarea asíncrona")
    except ValueError as e:
        print(f"Error capturado en async: {e}")

asyncio.run(tarea())


import psycopg2

try:
    conn = psycopg2.connect("dbname = empresa user = admin password = 123")
except psycopg2.OperationalError as e:
    print(f"Error de conexión contra la BD: {e}")
    


try:
    with open("archivo.csv", "r") as file:
        data = file.readline()
except FileNotFoundError:
    print("El archivo no existe")

# try, except, else, finally, logging

"""

import logging

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers= [
                        logging.FileHandler("Errores.log"),
                        logging.StreamHandler()
                        ]
)
try:
    with open("archivo.csv", "r") as file:
        data = file.readline()
except FileNotFoundError:
    logging.error("ERROR. El archivo no existe.")
    data = None
else:
    logging.info("El archivo fue leido con exito.")
finally:
    if data:
        data.close()