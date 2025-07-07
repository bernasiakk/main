def rotate(text, key):
    """
    TODO TODO I think it's pretty much it... Just fix the TODO's below, then run the tests, pylint and that's it.
    ---
    - TODO handle the spaces, numbers & special chars (you'll have to remove, then return them in the right places)
    """
    if not isinstance(key, int):
        raise TypeError("Key must be an integer.")
    
    if key > 27:
        raise ValueError("Key must be of length less than 28.")
    
    plain_list = list("abcdefghijklmnopqrstuvwxyz")
    # TODO I think you can remove this one, actually
    cipher_list = [plain_list[:] for _ in range(key)]
        
    # TODO change name
    result = []
    
    for letter in text:
        result.append(plain_list[plain_list.index(letter) + key])
    
    return ''.join(result)
    
    
if __name__ == "__main__":
    print(rotate('omg', 5))