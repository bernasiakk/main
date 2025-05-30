from typing import List, Union

def is_triangle(sides: List[Union[int, float]]) -> bool:
    """
    Validates if the given sides can form a triangle.
    
    Args:
        sides: List of three numbers representing triangle sides
    
    Returns:
        bool: True if sides can form a triangle
        
    Raises:
        TypeError: If values are not numbers or are less than 0
        Exception: If list length is not 3 or sides cannot form a triangle
    """
    if not all(isinstance(x, (int, float)) and x > 0 for x in sides):
        raise TypeError("Values must be of int or float type greater than 0.")

    if len(sides) != 3:
        raise Exception("A list of three values must be given as an argument.")
    
    a, b, c = sides
    if (a + b) < c or (a + c) < b or (b + c) < a:
        raise Exception("Values cannot form a triangle. please check")
    
    return True

def equilateral(sides: List[Union[int, float]]) -> bool:
    """Check if triangle is equilateral."""
    a, b, c = sides
    return is_triangle(sides) and a == b == c

def isosceles(sides: List[Union[int, float]]) -> bool:
    """Check if triangle is isosceles."""
    a, b, c = sides
    return is_triangle(sides) and (a == b or a == c or b == c)

def scalene(sides: List[Union[int, float]]) -> bool:
    """Check if triangle is scalene."""
    is_triangle(sides)
    return not (isosceles(sides) or equilateral(sides))


if __name__ == "__main__":
    print(scalene([[1,2,3],6,6]))