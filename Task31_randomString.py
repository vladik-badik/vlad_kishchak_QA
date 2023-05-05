import random

def get_random_string(length):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)] + \
               [chr(i) for i in range(ord('A'), ord('Z')+1)] + \
               [str(i) for i in range(10)]
    result = ''
    for i in range(length):
        result += random.choice(alphabet)
    return result
print(get_random_string(20))