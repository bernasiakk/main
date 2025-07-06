import re

def is_valid(isbn):
    isbn = str(isbn)
    
    # TODO change this so it checks if X is only at the last place??
    if not re.fullmatch(r"[0-9X\-]+", isbn):
        return False
    
    isbn = re.sub('[^0-9X]','', isbn)
    
    
    if not len(isbn) == 10:
        return False

    isbn = list(isbn)

    if 'X' in isbn:
        if not isbn[-1] == 'X':
            return False
        isbn[-1] = '10'
    
    # TODO list comprehension
    isbn_sum = 0
    
    for number, weight in zip(isbn, range(10,0,-1)):
        isbn_sum += int(number) * weight
    
    if isbn_sum % 11 == 0:
        return True
    return False
        

if __name__ == "__main__":
    print(is_valid("3-598-21508-8"))