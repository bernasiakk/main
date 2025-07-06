import pytest
from scripts.perfect_number import classify

def test_perfect():
    assert classify(6) == 'perfect'
    assert classify(28) == 'perfect'


def test_abundant():
    assert classify(12) == 'abundant'
    assert classify(24) == 'abundant'

def test_deficient():
    assert classify(8) == 'deficient'
    assert classify(1) == 'deficient'

def test_score_errors():
    with pytest.raises(TypeError):
        classify(-1)
        classify(0)
        classify("6")
        classify(3.14)