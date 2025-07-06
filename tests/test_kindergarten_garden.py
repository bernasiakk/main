import pytest
from scripts.kindergarten_garden import Garden

def test_wrong_inputs():
    with pytest.raises(ValueError):
        Garden(diagram='test', students=None)

def test_correct_outputs():
    # Arrange
    diagram = "VRCC\nVCGG"
    students = ["Valorie", "Raven"]
    expected_plants = ['Violets', 'Radishes', 'Violets', 'Clover']
    
    # Act
    garden = Garden(diagram=diagram, students=students)
    actual_plants = garden.plants("Raven")
    
    # Assert
    assert actual_plants == expected_plants

def test_default_students():
    # Arrange
    diagram = "VRCG\nVRCG"
    garden = Garden(diagram=diagram)
    
    # Act
    alice_plants = garden.plants("Alice")
    bob_plants = garden.plants("Bob")
    
    # Assert
    assert alice_plants == ['Violets', 'Radishes', 'Violets', 'Radishes']
    assert bob_plants == ['Clover', 'Grass', 'Clover', 'Grass']

def test_small_garden():
    # Arrange
    diagram = "GC\nGG"
    students = ["Anna", "Bob"]
    garden = Garden(diagram=diagram, students=students)
    
    # Act & Assert
    assert garden.plants("Anna") == ['Grass', 'Clover', 'Grass', 'Grass']
    assert garden.plants("Bob") == []  # Bob's position is beyond the garden width

def test_sorted_students():
    # Arrange
    diagram = "VVCC\nVVCC"
    students = ["Charlie", "Alice", "Bob"]  # Unsorted list
    garden = Garden(diagram=diagram, students=students)
    
    # Act & Assert
    # Alice should get first plants because students are sorted alphabetically
    assert garden.plants("Alice") == ['Violets', 'Violets', 'Violets', 'Violets']
    assert garden.plants("Bob") == ['Clover', 'Clover', 'Clover', 'Clover']
    assert garden.plants("Charlie") == []  # Beyond garden width

def test_all_plant_types():
    # Arrange
    diagram = "VRGC\nVRGC"
    garden = Garden(diagram=diagram, students=["Test"])
    
    # Act
    plants = garden.plants("Test")
    
    # Assert
    assert all(plant in ['Violets', 'Radishes', 'Grass', 'Clover'] for plant in plants)
    assert len(plants) == 4

def test_invalid_diagram_chars():
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        Garden("ABCD\nEFGH", students=["Test"])  # Invalid plant characters