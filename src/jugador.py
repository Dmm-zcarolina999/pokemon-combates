# jugador.py - Clase Jugador y selección de equipo.

TAM_EQUIPO = 3  # Número de criaturas por equipo


class Jugador:
    """Un jugador con un nombre y un equipo de criaturas."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []  # Lista de objetos Criatura

    def agregar_criatura(self, criatura):
        """Añade una criatura al equipo. Lanza ValueError si el equipo está lleno."""
        if self.equipo_completo():
            raise ValueError(f"El equipo de {self.nombre} ya tiene {TAM_EQUIPO} criaturas.")
        self.equipo.append(criatura)

    def equipo_completo(self):
        """True si el equipo ya tiene las 3 criaturas."""
        return len(self.equipo) >= TAM_EQUIPO

    def ha_perdido(self):
        """True si todas las criaturas del equipo están debilitadas."""
        return self.equipo_completo() and all(c.esta_debilitada() for c in self.equipo)
