def is_triangle(sides):
    if not all(isinstance(x, (int, float)) and x > 0 for x in sides):
        raise TypeError("Values must be of int or float type greater than 0.")

    if len(sides) != 3:
        raise Exception("A list of three values must be given as an argument.")
    
    a, b, c = sides[0], sides[1], sides[2]

    if (a + b) < c or (a + c) < b or (b + c) < a:
        raise Exception("Values cannot form a triangle. please check")
    
    return True

def equilateral(sides):
    a, b, c = sides[0], sides[1], sides[2]
    
    if is_triangle(sides) and a == b and b == c:
        return True

    return False

def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]

    if is_triangle(sides) and a == b or a == c or b == c:
        return True
    
    return False

def scalene(sides):
    is_triangle(sides)

    if isosceles(sides) or equilateral(sides):
        return False
    
    return True


if __name__ == "__main__":
    print(scalene([[1,2,3],6,6]))