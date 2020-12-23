from math import sqrt, ceil, floor

def is_square(n):
    return False if n < 0 else True if floor(sqrt(n)) == ceil(sqrt(n)) else False

if __name__ == "__main__":
    print(is_square(-1))
    print(is_square(4))
    print(is_square(3))