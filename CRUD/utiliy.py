import random
import string

def random_string(panjang):
    valueSTR =  ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return valueSTR