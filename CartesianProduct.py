from itertools import product
def CartesianProduct(s1, s2):
    """
    Given two lists in as a string, compute their Cartesian product
    """
    return ' '.join(map(str, product(map(int, s1.split()), map(int, s2.split()))))

if __name__ == "__main__":
    print(CartesianProduct('1 2', '3 4'))