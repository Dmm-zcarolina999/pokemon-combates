# Tests de la clase Criatura y de la carga del catálogo.
import os
import sys
import unittest

# Para poder importar los módulos de src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from criaturas import Criatura, cargar_criaturas


class TestCriatura(unittest.TestCase):
    def test_creacion(self):
        c = Criatura("Llamín", "Fuego", 90, 60, 45, 65)
        self.assertEqual(c.nombre, "Llamín")
        self.assertEqual(c.tipo, "Fuego")
        self.assertEqual(c.ps, 90)
        self.assertEqual(c.ps_max, 90)
        self.assertEqual(c.velocidad, 65)

    def test_str_contiene_nombre(self):
        self.assertIn("Llamín", str(Criatura("Llamín", "Fuego", 90, 60, 45, 65)))


class TestCarga(unittest.TestCase):
    def test_carga_catalogo(self):
        criaturas = cargar_criaturas()
        self.assertGreaterEqual(len(criaturas), 6)
        self.assertTrue(all(isinstance(c, Criatura) for c in criaturas))

    def test_valores_numericos(self):
        for c in cargar_criaturas():
            self.assertGreater(c.ps, 0)
            self.assertIsInstance(c.ataque, int)


if __name__ == "__main__":
    unittest.main()
