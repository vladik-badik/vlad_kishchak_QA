from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@memoize
def sequence (a,b,c):
    if c==0:
        return a
    else:
        return (a**c*b*c)

print(sequence(2,2,0))
print(sequence(2,2,3))
print(sequence(2,2,3))
print(sequence(1,2,5))

