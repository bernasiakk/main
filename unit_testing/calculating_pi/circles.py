from math import pi

def circle_area(r):
    if r <= 0:
        raise ValueError("r must be a positive number")
    elif not isinstance(r, (int, float)):
        raise Exception("r must be a number")
    return pi*(r**2)