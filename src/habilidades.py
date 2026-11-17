# habilidades.py - Clase Habilidad y carga del catálogo.
import csv
import os
import random

RUTA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


class Habilidad:
    """Un ataque que una criatura puede usar."""

    def __init__(self, nombre, tipo, poder, precision, pp):
        self.nombre = nombre          # Nombre del ataque
        self.tipo = tipo              # Tipo del ataque (Fuego, Agua...)
        self.poder = poder            # Fuerza base del ataque
        self.precision = precision    # Probabilidad de acertar (0-100)
        self.pp_max = pp              # Usos máximos (puntos de poder)
        self.pp = pp                  # Usos que quedan

    def __str__(self):
        """Texto para mostrar la habilidad por pantalla."""
        return (f"{self.nombre} ({self.tipo}) Poder {self.poder} "
                f"Prec {self.precision}% PP {self.pp}/{self.pp_max}")

    def tiene_pp(self):
        """True si todavía quedan usos."""
        return self.pp > 0

    def gastar_pp(self):
        """Gasta un uso. Lanza ValueError si no quedan PP."""
        if not self.tiene_pp():
            raise ValueError(f"{self.nombre} no tiene PP")
        self.pp -= 1

    def acierta(self):
        """Tirada de precisión: True si el ataque acierta."""
        return random.randint(1, 100) <= self.precision


def cargar_habilidades(ruta=None):
    """Lee data/habilidades.csv y devuelve un diccionario {nombre: Habilidad}."""
    if ruta is None:
        ruta = os.path.join(RUTA_DATOS, "habilidades.csv")
    habilidades = {}
    with open(ruta, newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            habilidades[fila["nombre"]] = Habilidad(
                fila["nombre"], fila["tipo"], int(fila["poder"]),
                int(fila["precision"]), int(fila["pp"]))
    return habilidades
