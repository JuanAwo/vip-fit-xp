import unittest
from python_project.src.motor_financiero import (
    calcular_van,
    calcular_tir,
    evaluar_van,
    evaluar_tir,
    generar_dictamen
)

class TestMotorFinanciero(unittest.TestCase):

    # 1. Lógica algorítmica VAN positivo
    def test_01_calcular_van_positivo(self):
        resultado = calcular_van(1000.0, 0.10, [600.0, 600.0])
        self.assertAlmostEqual(resultado, 41.322314, places=4)

    # 2. Lógica algorítmica VAN negativo
    def test_02_calcular_van_negativo(self):
        resultado = calcular_van(2000.0, 0.10, [500.0, 500.0])
        self.assertLess(resultado, 0)

    # 3. Prueba de límite (Boundary): Inversión inicial cero o negativa
    def test_03_van_inversion_invalida(self):
        with self.assertRaises(ValueError):
            calcular_van(0.0, 0.10, [500.0, 500.0])

    # 4. Prueba de límite (Boundary): Tasa de descuento menor o igual a -1
    def test_04_van_tasa_descuento_invalida(self):
        with self.assertRaises(ValueError):
            calcular_van(1000.0, -1.0, [500.0, 500.0])

    # 5. Control de excepciones: Lista de flujos vacía
    def test_05_van_flujos_vacios(self):
        with self.assertRaises(ValueError):
            calcular_van(1000.0, 0.10, [])

    # 6. Lógica algorítmica TIR por bisección
    def test_06_calcular_tir_valida(self):
        tir = calcular_tir(1000.0, [600.0, 600.0])
        self.assertIsNotNone(tir)
        self.assertAlmostEqual(tir, 0.130662, places=4)

    # 7. Caso borde TIR: Sin cambio de signo (flujos todos negativos)
    def test_07_tir_sin_raiz_en_intervalo(self):
        tir = calcular_tir(1000.0, [-200.0, -300.0])
        self.assertIsNone(tir)

    # 8. Regla de negocio: Clasificación del VAN con tolerancia
    def test_08_evaluar_van_reglas(self):
        self.assertEqual(evaluar_van(150.0), "Viable")
        self.assertEqual(evaluar_van(0.0000001), "Indiferente")
        self.assertEqual(evaluar_van(-50.0), "No viable")

    # 9. Regla de negocio: Clasificación de la TIR frente a tasa de descuento
    def test_09_evaluar_tir_reglas(self):
        self.assertEqual(evaluar_tir(0.15, 0.10), "Aceptable")
        self.assertEqual(evaluar_tir(0.08, 0.10), "Insuficiente")

    # 10. Motor de decisión integrado: Dictamen consolidado
    def test_10_generar_dictamen_consolidado(self):
        self.assertEqual(generar_dictamen("Viable", "Aceptable"), "Viable")
        self.assertEqual(generar_dictamen("No viable", "Insuficiente"), "No viable")
        self.assertEqual(generar_dictamen("Viable", "Insuficiente"), "Viabilidad condicionada")

if __name__ == '__main__':
    unittest.main()