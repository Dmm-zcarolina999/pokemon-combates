# main.py - Punto de entrada del juego.
# Se ejecuta con: python src/main.py
from jugador import pedir_numero


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


def jugar():
    """Inicia una partida (se completa con el modo dos jugadores)."""
    print("\nEl modo de juego todavía no está disponible.")


def ver_historial():
    """Muestra el historial de combates (se completa más adelante)."""
    print("\nEl historial todavía no está disponible.")


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
