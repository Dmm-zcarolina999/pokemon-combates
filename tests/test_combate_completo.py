# Test de un combate completo con decisiones automáticas.
import os
import random
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from combate import Combate, guardar_historial, leer_historial
from criaturas import cargar_criaturas


def jugar_combate_automatico(combate):
    """Juega hasta el final: siempre ataca con una habilidad al azar."""
    while not combate.terminado():
        for i in (0, 1):
            if combate.necesita_cambio(i):
                vivo = [n for n, c in enumerate(combate.equipos[i]) if not c.esta_debilitada()][0]
                combate.cambiar(i, vivo)
        combate.turno(("atacar", random.randrange(4)), ("atacar", random.randrange(4)))


class TestCombateCompleto(unittest.TestCase):
    def crear_combate(self):
        criaturas = cargar_criaturas()
        return Combate(criaturas[:3], criaturas[3:6], "Ana", "Bea")

    def test_termina_con_ganador(self):
        random.seed(1)
        combate = self.crear_combate()
        jugar_combate_automatico(combate)
        self.assertTrue(combate.terminado())
        self.assertIn(combate.ganador(), (0, 1))
        perdedor = 1 - combate.ganador()
        self.assertTrue(combate.equipo_derrotado(perdedor))

    def test_varias_semillas(self):
        for semilla in range(20):
            random.seed(semilla)
            combate = self.crear_combate()
            jugar_combate_automatico(combate)
            self.assertIsNotNone(combate.ganador())

    def test_registro_de_turnos(self):
        random.seed(2)
        combate = self.crear_combate()
        jugar_combate_automatico(combate)
        self.assertGreater(combate.numero_turno, 0)
        texto = combate.texto_registro()
        self.assertIn("Turno 1", texto)
        self.assertIn("usa", texto)

    def test_cambio_de_criatura(self):
        combate = self.crear_combate()
        combate.turno(("cambiar", 1), ("atacar", 0))
        self.assertEqual(combate.activos[0], 1)

    def test_cambio_invalido(self):
        combate = self.crear_combate()
        with self.assertRaises(ValueError):
            combate.cambiar(0, 0)  # Ya está en combate

    def test_historial(self):
        random.seed(3)
        combate = self.crear_combate()
        jugar_combate_automatico(combate)
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "historial.csv")
            guardar_historial(combate, ruta)
            filas = leer_historial(ruta)
        self.assertEqual(len(filas), 1)
        self.assertEqual(filas[0]["jugador1"], "Ana")


if __name__ == "__main__":
    unittest.main()
