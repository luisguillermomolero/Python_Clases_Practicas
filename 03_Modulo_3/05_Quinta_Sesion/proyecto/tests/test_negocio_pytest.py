import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorBase, VendedorPremium

import pytest

def test_calcular_comision_base():
    vendedor = VendedorBase("Juan", 1000)
    assert vendedor.calcular_comision() == 100.0

def test_calcular_comision_premium():
    vendedor = VendedorPremium("Maria", 2000)
    assert vendedor.calcular_comision() == 300.0
