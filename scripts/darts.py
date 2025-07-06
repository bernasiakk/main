import math

def score(x, y):
    # Validate inputs are real numbers
    if not (math.isfinite(x) and math.isfinite(y)):
        raise TypeError("Coordinates must be real numbers")
    
    distance =  math.sqrt(x**2+y**2)

    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    return 0


if __name__ == "__main__":
    print(score(1, 0.5))