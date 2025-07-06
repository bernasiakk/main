def primes(limit):
    """
    - write out all the numbers from 2 up to and including the number
    - 
    """
    
    numbers = list(range(2,limit+1))
    
    prime_numbers = []
    
    # sth = len(numbers)
    
    while numbers:
        for n in range(1,len(numbers)//2):
            for multiple in range(n * 2, limit + 1, n):
                numbers.remove(multiple)
                print(f"removed {multiple}, remaining list: {numbers}")

    
    # m = limit // 2 # TODO rename it
    
    
        

if __name__ == "__main__":
    primes(10)