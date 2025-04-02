import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorBase, VendedorPremium
import unittest

class TestVendedor(unittest.TestCase):
    
    def setUp(self):
        self.vendedor_base = VendedorBase("Luisito", 1000)
        self.vendedor_premiun = VendedorPremium("Carlitos",1000)
    
    def test_calcular_comision_base(self):
        self.assertEqual(self.vendedor_base.calcular_comision(), 100.0)
    
    def test_calcular_comision_premium(self):
        self.assertEqual(self.vendedor_premiun.calcular_comision(), 150.0)

if __name__ == '__main__':
    unittest.main()