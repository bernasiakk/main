def rotate(text, key):
    """
    """
    if not isinstance(key, int):
        raise TypeError("Key must be an integer.")
    
    if key > 27:
        raise ValueError("Key must be of length less than 28.")
    
    plain_list = list("abcdefghijklmnopqrstuvwxyz")*2

    result = []
    
    # TODO list comprehension??
    # TODO TODO test if this one handles numbers and special chars. Then think how to handle UPPERCASE letters
    for item in text:
        if item in plain_list:
            result.append(plain_list[plain_list.index(item) + key])
        else:
            result.append(item)
    
    return ''.join(result)
    
    
if __name__ == "__main__":
    print(rotate('omy', 5))