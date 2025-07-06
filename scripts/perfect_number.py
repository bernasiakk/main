def classify(number: int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Validate inputs are real numbers
    if number <= 0:
        raise TypeError("Number must be a positive int")
    
    if number == 1:
        return 'deficient'

    factors = [1]

    factor_check = number // 2

    while factor_check > 1:
        if number % factor_check == 0:
            factors.append(factor_check)
        factor_check -= 1
    
    if sum(factors) == number:
        return 'perfect'
    elif sum(factors) > number:
        return 'abundant'
    elif sum(factors) < number:
        return 'deficient'