import math
from itertools import zip_longest
import re

def cipher_text(plain_text):   
    stripped_text = re.sub(r'[^a-zA-Z0-9]', '', plain_text).lower()

    if not stripped_text:
        return ""
   
    length = len(stripped_text)
    square_root = math.sqrt(length)
    c = int(round(square_root))
    print(f'no of cols: {c}')
    r = int(round(length/c))

    rows = [stripped_text[i:i+c] for i in range(0, len(plain_text), c)]
    print(rows)

    rows_zipped = zip_longest(*rows, fillvalue='')

    code_zipped = ''.join(''.join(col) for col in rows_zipped)

    code_in_chunks = [code_zipped[i:i+r] for i in range(0, len(code_zipped), r)]
    
    final_code = ' '.join(code_in_chunks)

    return f"reponse: '{final_code}'"

# print(cipher_text('If man was meant to stay on the ground, god would have given us roots.'))
print(cipher_text('If man was meant to stay on the ground, god would have given us roots.'))