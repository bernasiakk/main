import re

def is_isogram(string):
    string = string.lower()
    
    if " " in string or "-" in string:
        string = re.split(r'[ -]', string)
        string = [word for sublist in string for word in sublist]
    
    return len(string) == len(set(string))
        
if __name__ == "__main__":
    print(is_isogram("test"))
