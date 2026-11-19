# Tests del cálculo de daño, la tabla de tipos y la gestión de PS.
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from combate import calcular_dano
from criaturas import Criatura
from habilidades import Habilidad
from tipos import TIPOS, multiplicador


class TestTipos(unittest.TestCase):
    def test_super_eficaz(self):
        self.assertEqual(multiplicador("Fuego", "Planta"), 2.0)
        self.assertEqual(multiplicador("Agua", "Fuego"), 2.0)

    def test_poco_eficaz(self):
        self.assertEqual(multiplicador("Fuego", "Agua"), 0.5)

    def test_normal(self):
        self.assertEqual(multiplicador("Normal", "Agua"), 1.0)

    def test_todos_los_tipos_tienen_multiplicador(self):
        for a in TIPOS:
            for d in TIPOS:
                self.assertGreaterEqual(multiplicador(a, d), 0)


class TestDano(unittest.TestCase):
    def setUp(self):
        self.atacante = Criatura("A", "Fuego", 100, 60, 50, 50)
        self.planta = Criatura("P", "Planta", 100, 50, 60, 50)
        self.agua = Criatura("W", "Agua", 100, 50, 60, 50)
        self.habilidad = Habilidad("Ascuas", "Fuego", 60, 100, 10)

    def test_super_eficaz_hace_mas_dano(self):
        self.assertGreater(calcular_dano(self.atacante, self.habilidad, self.planta),
                           calcular_dano(self.atacante, self.habilidad, self.agua))

    def test_valor_exacto(self):
        # 60/60 * 60 / 3 = 20, x2 por ser Fuego contra Planta
        self.assertEqual(calcular_dano(self.atacante, self.habilidad, self.planta), 40)

    def test_dano_minimo_uno(self):
        debil = Habilidad("Nada", "Normal", 1, 100, 10)
        self.assertEqual(calcular_dano(self.atacante, debil, self.planta), 1)


class TestPuntosDeSalud(unittest.TestCase):
    def setUp(self):
        self.c = Criatura("A", "Fuego", 100, 60, 50, 50)

    def test_recibir_dano(self):
        self.assertEqual(self.c.recibir_dano(30), 30)
        self.assertEqual(self.c.ps, 70)

    def test_ps_no_bajan_de_cero(self):
        self.c.recibir_dano(500)
        self.assertEqual(self.c.ps, 0)
        self.assertTrue(self.c.esta_debilitada())

    def test_curar_no_pasa_del_maximo(self):
        self.c.recibir_dano(10)
        self.assertEqual(self.c.curar(50), 10)
        self.assertEqual(self.c.ps, 100)

    def test_debilitada_no_se_cura(self):
        self.c.recibir_dano(500)
        self.assertEqual(self.c.curar(50), 0)


class TestHabilidad(unittest.TestCase):
    def test_pp(self):
        h = Habilidad("X", "Normal", 40, 100, 2)
        h.gastar_pp()
        h.gastar_pp()
        self.assertFalse(h.tiene_pp())
        with self.assertRaises(ValueError):
            h.gastar_pp()

    def test_precision_extremos(self):
        self.assertTrue(all(Habilidad("X", "Normal", 40, 100, 1).acierta() for _ in range(50)))
        self.assertFalse(any(Habilidad("X", "Normal", 40, 0, 1).acierta() for _ in range(50)))


if __name__ == "__main__":
    unittest.main()
