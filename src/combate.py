# combate.py - Motor de combate: cálculo de daño y turnos.
import random

from tipos import multiplicador


def calcular_dano(atacante, habilidad, defensor):
    """Calcula el daño de una habilidad.

    Fórmula: (ataque / defensa) * poder / 3 * multiplicador de tipo.
    Si el tipo no hace efecto (x0) el daño es 0; en cualquier otro caso
    el daño mínimo es 1.
    """
    mult = multiplicador(habilidad.tipo, defensor.tipo)
    if mult == 0:
        return 0
    base = atacante.ataque / defensor.defensa * habilidad.poder / 3
    return max(1, int(base * mult))


def orden_turno(criatura1, criatura2):
    """Decide quién actúa primero según la velocidad.

    Devuelve (0, 1) si va primero la criatura 1 o (1, 0) si va primero la 2.
    Si hay empate de velocidad se decide al azar.
    """
    if criatura1.velocidad > criatura2.velocidad:
        return (0, 1)
    if criatura2.velocidad > criatura1.velocidad:
        return (1, 0)
    return random.choice([(0, 1), (1, 0)])
