# Tests de control de errores.
import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from criaturas import cargar_criaturas
from jugador import Jugador, pedir_numero


class TestErrores(unittest.TestCase):
    def test_pedir_numero_ignora_entradas_invalidas(self):
        with mock.patch("builtins.input", side_effect=["", "abc", "-1", "9", "3"]):
            with mock.patch("builtins.print"):
                self.assertEqual(pedir_numero("> ", 1, 5), 3)

    def test_csv_inexistente(self):
        with self.assertRaises(OSError):
            cargar_criaturas("no_existe.csv")

    def test_equipo_lleno(self):
        jugador = Jugador("Ana")
        for criatura in cargar_criaturas()[:3]:
            jugador.agregar_criatura(criatura)
        with self.assertRaises(ValueError):
            jugador.agregar_criatura(cargar_criaturas()[3])


if __name__ == "__main__":
    unittest.main()
