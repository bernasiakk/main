from math import pi

def circle_area(r):
    if r <= 0:
        raise Exception("r must be a positive number")
    return pi*(r**2)