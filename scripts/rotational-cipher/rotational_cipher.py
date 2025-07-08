def rotate(text, key):
    """Rotate the given text by the specified key using a rotational cipher."""
    if not isinstance(key, int):
        raise TypeError("Key must be an integer.")
    if key > 27:
        raise ValueError("Key must be less than 28.")

    plain_list = list("abcdefghijklmnopqrstuvwxyz") * 2
    result = []

    for item in text:
        if item in plain_list:
            result.append(plain_list[plain_list.index(item) + key])
        elif item.lower() in plain_list:
            result.append(plain_list[plain_list.index(item.lower()) + key].upper())
        else:
            result.append(item)

    return ''.join(result)


if __name__ == "__main__":
    print(rotate('Omy-omy', 5))
