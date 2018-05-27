import pytest

from x import *

def test_product():
    assert product(5) == 25
    assert not product(2) == 5
    assert product(-3) == 9
