# Reglas del juego

## Objetivo
Dejar sin puntos de salud (PS) a las 3 criaturas del rival.

## Preparación
1. Cada jugador escribe su nombre.
2. Cada jugador elige 3 criaturas distintas del catálogo (`data/criaturas.csv`).
3. Empieza luchando la primera criatura elegida de cada equipo.

## Criaturas
Tienen nombre, tipo, PS, ataque, defensa, velocidad y 4 habilidades.

## Turnos
En cada turno los dos jugadores eligen (uno detrás de otro) una de estas acciones:
- **Usar una habilidad** de su criatura activa.
- **Cambiar de criatura** por otra del equipo que no esté debilitada. Cambiar
  sustituye al ataque de ese turno y ocurre antes de los ataques.

Los ataques se ejecutan por orden de **velocidad**: la criatura más rápida
actúa primero. Si hay empate se decide al azar. Una criatura que se debilita
antes de actuar pierde su ataque.

## Habilidades
- **Poder:** fuerza base del ataque.
- **Precisión:** probabilidad (%) de acertar. Si falla no hace daño.
- **PP:** usos disponibles. Cada uso gasta 1 PP aunque falle. Sin PP no se puede
  usar. Si a una criatura no le queda ningún PP, usa *Forcejeo* (poder 40).

## Cálculo del daño
    daño = (ataque / defensa) * poder / 3 * multiplicador de tipo
El daño se redondea hacia abajo y es **como mínimo 1** (salvo que el
multiplicador sea 0).

## Tipos
Multiplicador según el tipo de la habilidad (fila) contra el tipo defensor (columna):

| Ataque \ Defensa | Fuego | Agua | Planta | Eléctrico | Normal |
|------------------|-------|------|--------|-----------|--------|
| Fuego            | x0.5  | x0.5 | x2     | x1        | x1     |
| Agua             | x2    | x0.5 | x0.5   | x1        | x1     |
| Planta           | x0.5  | x2   | x0.5   | x1        | x1     |
| Eléctrico        | x1    | x2   | x0.5   | x0.5      | x1     |
| Normal           | x1    | x1   | x1     | x1        | x1     |

## Criatura debilitada
Cuando una criatura llega a 0 PS se debilita y su dueño debe sacar otra.
No se puede curar una criatura debilitada.

## Fin del combate
Gana el jugador que deja debilitado al equipo rival. El resultado se guarda en
`data/historial.csv` y se puede consultar desde el menú.

## Ejemplo de turno
Llamín (Fuego, VEL 65) usa *Ascuas* contra Hojín (Planta, VEL 45):
1. Llamín es más rápido, así que ataca primero.
2. Fuego contra Planta es x2, por lo que el daño se duplica.
3. Después ataca Hojín con la habilidad que haya elegido.
