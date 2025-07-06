import re

def is_valid(isbn):
    """
    - [x] verify that only hyphens and digits are there
    - [x] clean the number from hyphens, etc.
    - [x] check that length is 10
    - [] check that the first 9 chars are numbers (and use that as a list called 9_digits)
    - [] take the last number (the 'check' number) as a separate variable
    - [] if X is in the last position string, convert it to 10 >> convert the variable to int()
    - [] for i, j in 9_digits, reversed(range(2,11))
    
    checks:
        - all numbers are 
        - length is
    """
    isbn = str(isbn)
    
    if not re.fullmatch(r"[0-9X\-]+", isbn):
        raise TypeError("ISBN must consist of only numbers, digits and X'es")
    
    # TODO include X in here also. Then, it will be easy to make sure it's at the last position only
    isbn = re.sub('[^0-9X]','', isbn)
    
    if not len(isbn) == 10:
        raise ValueError("ISBN must be a length of 10 (excl. dashes)")
    
    # TODO add checks (i.e., if not isinstance(main_numbers, digits)...)
    
    # TODO list comprehension
    # TODO change this 'j' to sth else
    isbn_sum = 0
    
    for number, j in zip(isbn, range(10,0,-1)):
        isbn_sum += int(number) * j
    
    if isbn_sum % 11 == 0:
        return True
    return False
        

if __name__ == "__main__":
    print(is_valid("3-598-21508-8"))