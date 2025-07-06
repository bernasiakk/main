import pytest
from scripts.crypto_square import cipher_text

# standard stuff
def test_proper_cipher_text():
    assert cipher_text('If man was meant to stay on the ground, god would have given us roots.') == 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau '

# special characters & numbers
def test_special_characters():
    assert cipher_text('If man#$^# was m3$eant to st^&$#ay on the ground, god66 would 3423have given us roots77451.') == 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau '

# upperccase to lowercase
def test_uppercase():
    assert cipher_text('IF MAN WAS MEANT TO STAY ON THE GROUND, GOD WOULD HAVE GIVEN US ROOTS.') == 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau '

# one character
def test_few_characters():
    assert cipher_text('g') == 'g '
    assert cipher_text('ghiy') == 'ghiy '
    assert cipher_text('ghiy') == 'ghiy '
    assert cipher_text('abcdefghij') == 'adgj behc fi '

# only special characters & numbers
def test_errors():
    with pytest.raises(TypeError):
        cipher_text(0)
        cipher_text('')
        cipher_text('2135&5')