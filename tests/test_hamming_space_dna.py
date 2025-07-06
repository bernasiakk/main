import pytest
from scripts.hamming_space_dna import distance

def test_correct_distance():
    assert distance('CCGT', 'CAGT') == 1
    assert distance('GGGG', 'GGGG') == 0  # identical strands
    assert distance('ACGT', 'TGCA') == 4  # completely different
    assert distance('GACT', 'GACT') == 0  # another identical case
    assert distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT') == 7  # longer sequence

def test_errors():
    with pytest.raises(ValueError):
        # Test invalid characters
        distance('XXXX', 'ACGT')
        
        # Test unequal lengths
        distance('CAAAAGT', 'GACT')  

        # Test empty strings
        distance('', '')

        # Test case sensitivity (if DNA should be uppercase)
        distance('acgt', 'ACGT')  

        # Test spaces and special characters
        distance('AC GT', 'ACGT')
