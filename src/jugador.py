# jugador.py - Clase Jugador y selección de equipo.
import copy

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


def pedir_numero(texto, minimo, maximo):
    """Pide un número entre minimo y maximo (ambos incluidos) hasta que sea válido."""
    while True:
        respuesta = input(texto).strip()
        if respuesta.isdigit() and minimo <= int(respuesta) <= maximo:
            return int(respuesta)
        print(f"Entrada no válida. Escribe un número entre {minimo} y {maximo}.")


def elegir_equipo(jugador, catalogo):
    """Deja que el jugador elija sus 3 criaturas del catálogo por número.

    Se guarda una copia de cada criatura para que no se compartan entre jugadores.
    """
    print(f"\n{jugador.nombre}, elige tus {TAM_EQUIPO} criaturas:")
    for numero, criatura in enumerate(catalogo, start=1):
        print(f"  {numero}. {criatura.nombre} ({criatura.tipo}) PS {criatura.ps_max} "
              f"ATQ {criatura.ataque} DEF {criatura.defensa} VEL {criatura.velocidad}")
    elegidas = []
    while len(elegidas) < TAM_EQUIPO:
        numero = pedir_numero(f"Criatura {len(elegidas) + 1}/{TAM_EQUIPO}: ", 1, len(catalogo))
        if numero in elegidas:
            print("Ya has elegido esa criatura.")
            continue
        elegidas.append(numero)
        jugador.agregar_criatura(copy.deepcopy(catalogo[numero - 1]))
