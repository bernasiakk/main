import pytest
from scripts.darts import score

def test_score():
    assert score(1, 0.5) == 5
    assert score(0, 10) == 1
    assert score(1, 20) == 0
    assert score(-1, -0.5) == 5
    assert score(-1, 0.5) == 5

def test_score_errors():
    with pytest.raises(TypeError):
        score('five', 10)
