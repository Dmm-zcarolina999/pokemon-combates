# criaturas.py - Clase Criatura y carga del catálogo.


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

    def __str__(self):
        """Texto para mostrar la criatura por pantalla."""
        return (f"{self.nombre} ({self.tipo}) PS {self.ps}/{self.ps_max} "
                f"ATQ {self.ataque} DEF {self.defensa} VEL {self.velocidad}")
