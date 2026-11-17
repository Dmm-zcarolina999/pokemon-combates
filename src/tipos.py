# tipos.py - Tipos de criaturas y tabla de efectividad.

# Lista de tipos del juego
TIPOS = ["Fuego", "Agua", "Planta", "Eléctrico", "Normal"]

# EFECTIVIDAD[tipo_atacante][tipo_defensor] = multiplicador de daño.
# Lo que no aparece en la tabla vale 1 (daño normal).
EFECTIVIDAD = {
    "Fuego":     {"Planta": 2.0, "Agua": 0.5, "Fuego": 0.5},
    "Agua":      {"Fuego": 2.0, "Planta": 0.5, "Agua": 0.5},
    "Planta":    {"Agua": 2.0, "Fuego": 0.5, "Planta": 0.5},
    "Eléctrico": {"Agua": 2.0, "Planta": 0.5, "Eléctrico": 0.5},
    "Normal":    {},
}


def multiplicador(tipo_ataque, tipo_defensor):
    """Devuelve cuánto daño multiplica un tipo de ataque contra un tipo defensor."""
    return EFECTIVIDAD.get(tipo_ataque, {}).get(tipo_defensor, 1.0)
