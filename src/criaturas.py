# criaturas.py - Clase Criatura y carga del catálogo.
import csv
import copy
import os

from habilidades import cargar_habilidades

# Carpeta data/ junto a src/ (funciona se ejecute desde donde se ejecute)
RUTA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


class Criatura:
    """Una criatura que puede combatir."""

    def __init__(self, nombre, tipo, ps, ataque, defensa, velocidad):
        self.nombre = nombre          # Nombre de la criatura
        self.tipo = tipo              # Tipo (Fuego, Agua...)
        self.ps_max = ps              # Puntos de salud máximos
        self.ps = ps                  # Puntos de salud actuales
        self.ataque = ataque          # Fuerza de ataque
        self.defensa = defensa        # Resistencia al daño
        self.velocidad = velocidad    # Quien tiene más velocidad ataca primero
        self.habilidades = []         # Lista de 4 objetos Habilidad

    def __str__(self):
        """Texto para mostrar la criatura por pantalla."""
        return (f"{self.nombre} ({self.tipo}) PS {self.ps}/{self.ps_max} "
                f"ATQ {self.ataque} DEF {self.defensa} VEL {self.velocidad}")

    def esta_debilitada(self):
        """Una criatura está debilitada cuando se queda sin PS."""
        return self.ps <= 0

    def recibir_dano(self, cantidad):
        """Resta PS (sin bajar de 0) y devuelve el daño realmente recibido."""
        perdido = min(max(cantidad, 0), self.ps)
        self.ps -= perdido
        return perdido

    def curar(self, cantidad):
        """Suma PS (sin pasar del máximo) y devuelve lo que se ha curado.
        Una criatura debilitada no se puede curar."""
        if self.esta_debilitada():
            return 0
        curado = min(max(cantidad, 0), self.ps_max - self.ps)
        self.ps += curado
        return curado


def cargar_criaturas(ruta=None):
    """Lee data/criaturas.csv y devuelve una lista de objetos Criatura."""
    if ruta is None:
        ruta = os.path.join(RUTA_DATOS, "criaturas.csv")
    habilidades = cargar_habilidades()
    criaturas = []
    with open(ruta, newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            criaturas.append(Criatura(
                fila["nombre"], fila["tipo"], int(fila["ps"]),
                int(fila["ataque"]), int(fila["defensa"]), int(fila["velocidad"])))
            # Cada criatura recibe su propia copia de cada habilidad (así
            # los PP de una criatura no afectan a otra)
            for nombre in fila["habilidades"].split(";"):
                criaturas[-1].habilidades.append(copy.deepcopy(habilidades[nombre]))
    return criaturas
