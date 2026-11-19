# main.py - Punto de entrada del juego.
# Se ejecuta con: python src/main.py
from combate import (Combate, cambiar_criatura, guardar_historial,
                     leer_historial, sin_pp)
from criaturas import cargar_criaturas
from jugador import Jugador, elegir_equipo, pedir_numero


def mostrar_reglas():
    """Muestra un resumen de las reglas."""
    print("\n--- Reglas básicas ---")
    print("- Cada jugador elige 3 criaturas y lucha con una a la vez.")
    print("- En cada turno eliges una habilidad o cambias de criatura.")
    print("- Ataca primero la criatura con más velocidad.")
    print("- Cada habilidad tiene PP (usos) y precisión (puede fallar).")
    print("- Algunos tipos son más fuertes contra otros (ej. Agua > Fuego).")
    print("- Gana quien deja sin PS a todas las criaturas rivales.")
    print("(Más detalle en docs/reglas.md)")


def pedir_accion(combate, i):
    """Pide al jugador i su acción del turno: atacar o cambiar de criatura."""
    activa = combate.activa(i)
    print(f"\n--- Turno de {combate.nombres[i]} ---")
    print(f"En combate: {activa}")
    while True:
        print("Habilidades:")
        for n, habilidad in enumerate(activa.habilidades, start=1):
            print(f"  {n}. {habilidad}")
        print("  5. Cambiar de criatura")
        opcion = pedir_numero("Elige: ", 1, 5)
        if opcion == 5:
            nuevo = pedir_sustituto(combate, i, permitir_volver=True)
            if nuevo is not None:
                return ("cambiar", nuevo)
        elif activa.habilidades[opcion - 1].tiene_pp() or sin_pp(activa):
            return ("atacar", opcion - 1)
        else:
            print("¡No quedan PP de esa habilidad!")


def pedir_sustituto(combate, i, permitir_volver=False):
    """Pide qué criatura sacar. Devuelve su índice (o None si el jugador vuelve atrás)."""
    equipo = combate.equipos[i]
    while True:
        print("Tu equipo:")
        for n, criatura in enumerate(equipo, start=1):
            marca = " (en combate)" if n - 1 == combate.activos[i] else ""
            print(f"  {n}. {criatura}{marca}")
        if permitir_volver:
            print("  0. Volver")
        numero = pedir_numero("Criatura: ", 0 if permitir_volver else 1, len(equipo))
        if numero == 0:
            return None
        try:
            cambiar_criatura(combate.equipos[i], combate.activos[i], numero - 1)
            return numero - 1
        except ValueError as error:
            print(error)


def jugar():
    """Partida de dos jugadores en el mismo teclado."""
    catalogo = cargar_criaturas()
    jugadores = []
    for n in (1, 2):
        nombre = input(f"\nNombre del jugador {n}: ").strip() or f"Jugador {n}"
        jugador = Jugador(nombre)
        elegir_equipo(jugador, catalogo)
        jugadores.append(jugador)
    combate = Combate(jugadores[0].equipo, jugadores[1].equipo,
                      jugadores[0].nombre, jugadores[1].nombre)
    print(f"\n¡Empieza el combate: {combate.nombres[0]} contra {combate.nombres[1]}!")
    while not combate.terminado():
        acciones = []
        for i in (0, 1):
            acciones.append(pedir_accion(combate, i))
            print("\n" * 30)  # Espacio para que el otro jugador no vea la elección
        print("".join(["=" for _ in range(40)]))
        for mensaje in combate.turno(*acciones):
            print(mensaje)
        # Si una criatura se ha debilitado hay que sacar otra
        for i in (0, 1):
            if combate.necesita_cambio(i):
                print(f"\n{combate.nombres[i]}, tu criatura está debilitada. Elige otra.")
                print(combate.cambiar(i, pedir_sustituto(combate, i)))
    print(f"\n¡{combate.nombres[combate.ganador()]} gana el combate en {combate.numero_turno} turnos!")
    guardar_historial(combate)


def ver_historial():
    """Muestra los combates guardados en data/historial.csv."""
    combates = leer_historial()
    print("\n--- Historial de combates ---")
    if not combates:
        print("Todavía no se ha jugado ningún combate.")
    for c in combates:
        print(f"{c['fecha']} | {c['jugador1']} vs {c['jugador2']} | "
              f"Gana {c['ganador']} ({c['turnos']} turnos)")


def menu():
    """Muestra el menú principal en bucle hasta que el usuario elige salir."""
    while True:
        print("\n=== Plataforma de Combates Pokémon ===")
        print("1. Jugar (2 jugadores)")
        print("2. Ver reglas")
        print("3. Ver historial de combates")
        print("4. Salir")
        opcion = pedir_numero("Elige una opción: ", 1, 4)
        if opcion == 1:
            jugar()
        elif opcion == 2:
            mostrar_reglas()
        elif opcion == 3:
            ver_historial()
        else:
            print("¡Hasta pronto!")
            break


def main():
    """Función principal del programa."""
    menu()


if __name__ == "__main__":
    main()
