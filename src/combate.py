# combate.py - Motor de combate: cálculo de daño y turnos.
import random

from habilidades import Habilidad
from tipos import multiplicador

# Ataque de emergencia cuando a una criatura no le quedan PP en ninguna habilidad
FORCEJEO = Habilidad("Forcejeo", "Normal", 40, 100, 999)


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


def sin_pp(criatura):
    """True si la criatura no tiene PP en ninguna de sus habilidades."""
    return not any(h.tiene_pp() for h in criatura.habilidades)


def usar_habilidad(atacante, habilidad, defensor):
    """Aplica una habilidad y devuelve la lista de mensajes de lo ocurrido."""
    if sin_pp(atacante):
        habilidad = FORCEJEO
    mensajes = []
    if not habilidad.tiene_pp():
        return [f"{atacante.nombre} no tiene PP en {habilidad.nombre} y pierde el turno."]
    habilidad.gastar_pp()
    mensajes.append(f"{atacante.nombre} usa {habilidad.nombre}.")
    if not habilidad.acierta():
        mensajes.append("¡Pero falla!")
        return mensajes
    mult = multiplicador(habilidad.tipo, defensor.tipo)
    dano = defensor.recibir_dano(calcular_dano(atacante, habilidad, defensor))
    if mult == 0:
        mensajes.append(f"No afecta a {defensor.nombre}...")
    else:
        if mult > 1:
            mensajes.append("¡Es muy eficaz!")
        elif mult < 1:
            mensajes.append("No es muy eficaz...")
        mensajes.append(f"{defensor.nombre} pierde {dano} PS ({defensor.ps}/{defensor.ps_max}).")
    if defensor.esta_debilitada():
        mensajes.append(f"¡{defensor.nombre} se debilita!")
    return mensajes


def ejecutar_turno(criatura1, habilidad1, criatura2, habilidad2):
    """Turno 1 contra 1: cada criatura usa su habilidad, la más rápida primero.

    Devuelve la lista de mensajes del turno.
    """
    criaturas = [criatura1, criatura2]
    habilidades = [habilidad1, habilidad2]
    mensajes = []
    for i in orden_turno(criatura1, criatura2):
        atacante, defensor = criaturas[i], criaturas[1 - i]
        if atacante.esta_debilitada():
            continue  # Si ya se ha debilitado en este turno no actúa
        mensajes += usar_habilidad(atacante, habilidades[i], defensor)
    return mensajes


def cambiar_criatura(equipo, activo, nuevo):
    """Comprueba el cambio de criatura y devuelve el índice de la nueva activa.

    equipo: lista de criaturas; activo: índice de la actual; nuevo: índice elegido.
    Lanza ValueError si el cambio no es posible.
    """
    if nuevo < 0 or nuevo >= len(equipo):
        raise ValueError("Esa criatura no existe.")
    if nuevo == activo:
        raise ValueError(f"{equipo[nuevo].nombre} ya está en combate.")
    if equipo[nuevo].esta_debilitada():
        raise ValueError(f"{equipo[nuevo].nombre} está debilitada.")
    return nuevo
