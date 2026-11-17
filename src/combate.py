# combate.py - Motor de combate: cálculo de daño y turnos.
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
