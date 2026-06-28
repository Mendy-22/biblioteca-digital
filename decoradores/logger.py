import functools
from datetime import datetime


def log_operacion(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] LOG: Ejecutando '{func.__name__}'...")
        resultado = func(*args, **kwargs)
        print(f"[{timestamp}] LOG: '{func.__name__}' finalizado correctamente")
        return resultado
    return wrapper
