import re
import datetime

def validar_telefono(telefono):
    """Valida un número de teléfono según un patrón."""
    return bool(re.match(r'^\+?\d{7,15}$', telefono))

def validar_fecha(fecha):
    """Valida una fecha según el formato YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora):
    """Valida una hora según el formato HH:MM."""
    return bool(re.match(r'^([01]?\d|2[0-3]):[0-5]\d$', hora))
