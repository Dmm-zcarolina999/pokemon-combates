# Plataforma de Combates Pokémon

Videojuego de combates por turnos en terminal. Dos jugadores eligen un equipo de
3 criaturas, usan habilidades, gestionan sus puntos de vida y se enfrentan.

Proyecto de clase de Entornos de Desarrollo (1º DAM).

## Requisitos
Python 3 (solo se usa la librería estándar, no hay que instalar nada).

## Cómo ejecutar

    python src/main.py

## Cómo ejecutar los tests

    python -m unittest discover tests

## Cómo se juega
Desde el menú elige **Jugar**, escribe los nombres y elige 3 criaturas cada uno.
En cada turno se elige una habilidad (1-4) o cambiar de criatura (5).
Las reglas completas están en [docs/reglas.md](docs/reglas.md).

## Estructura

| Ruta | Contenido |
|------|-----------|
| `src/main.py` | Menú y partida de dos jugadores |
| `src/criaturas.py` | Clase `Criatura` y carga del catálogo |
| `src/habilidades.py` | Clase `Habilidad` (PP, precisión) |
| `src/tipos.py` | Tipos y tabla de efectividad |
| `src/combate.py` | Cálculo de daño, turnos, clase `Combate`, historial |
| `src/jugador.py` | Clase `Jugador` y selección de equipo |
| `data/` | `criaturas.csv`, `habilidades.csv`, `historial.csv` |
| `tests/` | Tests con unittest |
| `docs/reglas.md` | Reglas del juego |

## Añadir criaturas o habilidades
Basta con añadir una fila a `data/criaturas.csv` (con 4 habilidades separadas
por `;`) o a `data/habilidades.csv`.

## Equipo
| Persona | Usuario de GitHub |
|---------|-------------------|
| Persona 1 | Dmm-zcarolina999 |
| Persona 2 | Gonzalo-udit |
| Persona 3 | colincumbicus-blip |
