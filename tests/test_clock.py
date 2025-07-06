import pytest
from scripts.clock import Clock

def test_repr_method():
    assert repr(Clock(10, 50)) == 'Clock(hour=10, minute=50)'

def test_str_method():
    assert str(Clock(10, 50)) == '10:50'
    
def test_adding_minutes():
    assert str(Clock(10, 50) + 1) == '10:51'
    assert str(Clock(10, 50) + 29) == '11:19'
    assert str(Clock(10, 50) + 1441) == '10:51'
        
def test_subtracting_minutes():
    assert str(Clock(10, 50) - 1) == '10:49'
    assert str(Clock(10, 50) - 51) == '9:59'
    assert str(Clock(10, 50) - 60) == '9:50'
    assert str(Clock(10, 50) - 1441) == '10:49'

def test_magic_method_patterns():
    clock = Clock(10, 50)
    
    # Pattern 1: Built-in functions ("around" the object)
    assert str(clock) == '10:50'
    assert repr(clock) == 'Clock(hour=10, minute=50)'
    
    # Pattern 2: Operators (infix notation)
    assert clock + 10 == Clock(11, 0)
    assert clock == Clock(10, 50)
    
def test_formatting():
    assert Clock(hour=11, minute=0) == Clock(hour=11, minute=00)
    assert Clock(hour=0, minute=0) == Clock(hour=00, minute=00)

def test_isinstance_behavior():
    clock = Clock(10, 50)
    assert isinstance(clock, Clock)  # true for Clock instances
    assert not isinstance("10:50", Clock)  # false for strings
    assert not isinstance(650, Clock)  # false for numbers

def test_errors():
    with pytest.raises(TypeError):
        Clock('five', 10)
        Clock(10, 'five')
        Clock(1.5, 2)
        Clock(1, 2.5)
        Clock(-1, 10)
        Clock(1, -10)
    
    with pytest.raises(ValueError):
        Clock(-1, 0)
        Clock(0, -1)
        Clock(25, 0)
        Clock(0, 25)

def test_wraparound_cases():
    # Test midnight wraparound
    assert str(Clock(23, 50) + 20) == "0:10"
    assert str(Clock(0, 10) - 20) == "23:50"
    
    # Test full day wraparound
    clock = Clock(0, 0)
    assert clock + 1440 == Clock(0, 0)  # 24 hours forward
    assert clock - 1440 == Clock(0, 0)  # 24 hours backward

def test_large_minute_changes():
    # Test multiple days forward
    assert Clock(0, 0) + 4320 == Clock(0, 0)  # 3 days forward
    # Test multiple days backward
    assert Clock(0, 0) - 4320 == Clock(0, 0)  # 3 days backward

def test_comparison_with_other_types():
    clock = Clock(11, 30)
    assert (clock == "11:30") is False
    assert (clock == 690) is False  # 11:30 in minutes
    assert (clock != "11:30") is True
    assert (clock != 690) is True

def test_edge_time_values():
    # Test exactly midnight
    assert str(Clock(0, 0)) == "0:0"
    # Test last minute of day
    assert str(Clock(23, 59)) == "23:59"
    # Test almost last minute
    assert str(Clock(23, 58)) == "23:58"