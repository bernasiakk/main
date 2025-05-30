def is_armstrong_number(number: int):
    digits_list = list(map(int, str(number)))

    total_value = 0

    for digit in digits_list:
        total_value += digit ** len(digits_list)
    
    return number == total_value


print(is_armstrong_number(152))