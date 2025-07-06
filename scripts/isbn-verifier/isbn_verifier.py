
"""Module for validating ISBN-10 numbers."""
import re

def is_valid(isbn):

    """Check if the provided ISBN-10 is valid."""
    isbn = str(isbn)

    # TODO Check if X is only at the last place
    if not re.fullmatch(r"[0-9X\-]+", isbn):
        return False

    isbn = re.sub(r'[^0-9X]', '', isbn)

    if len(isbn) != 10:
        return False

    isbn = list(isbn)

    if 'X' in isbn:
        if isbn[-1] != 'X':
            return False
        isbn[-1] = '10'

    # Use list comprehension for sum
    isbn_sum = sum(int(number) * weight for number, weight in zip(isbn, range(10, 0, -1)))

    return isbn_sum % 11 == 0


if __name__ == "__main__":
    print(is_valid("3-598-21508-8"))
