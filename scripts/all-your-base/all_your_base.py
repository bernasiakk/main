from itertools import dropwhile


def rebase(input_base: int, digits: list, output_base: int) -> list:
    """
    main:
    - [] calculate initial number using digits and input base:
        - [] have a initial_number = 0
        - [] reverse a list of digits
        - [] have a for loop with range(len(digits)) and reversed_list:
            >> add your calc (initial_number += i + digit)
    - [] get final number using output base
        - [] final_number = []
        - [] while calculated_number > 0:
            
            final_number.append(calculated_number % output_base)
            calculated_number -= calculated_number // output_base
        - [] reverse final_number, that's your output
   ---
   write checks:
    - [] digits must be a list
    - [] 
    """   
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not isinstance(digits, list) or not all(isinstance(d, int) for d in digits):
        raise ValueError("digits must be a list of integers")
    
    # Remove leading zeros
    digits = list(dropwhile(lambda x: x == 0, digits))
    
    if not digits:
        return [0]

    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    

    # Convert to integer
    calculated_number = 0
    
    for digit in digits:
        calculated_number = calculated_number * input_base + digit
    
    # Convert to output base
    if calculated_number == 0:
        return [0]
    
    final_number = []
    
    while calculated_number > 0:
        final_number.append(calculated_number % output_base)
        calculated_number //= output_base
    
    return final_number[::-1]


if __name__ == "__main__":
    print(rebase(2, [1, 0, 1, 0, 1, 0], 10))