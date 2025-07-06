def is_pangram(sentence):
    english_alphabet = ["a","b","c","d","e","f","g","h","i",
                        "j","k","l","m","n","o","p","q","r",
                        "s","t","u","v","w","x","y","z"]
    
    list_of_unique_chars_and_signs = set(sentence.lower())
    
    list_of_unique_chars = [l for l in list_of_unique_chars_and_signs if l in english_alphabet]
    
    return set(english_alphabet) == set(list_of_unique_chars)
    
if __name__ == "__main__":
    print(is_pangram('The quick brown fox jumps over the lazy dog.'))