# habilidades.py - Clase Habilidad y carga del catálogo.


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
