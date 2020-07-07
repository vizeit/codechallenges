def summation(l):
    """
    Given a list of elements with sublists, return total
    """
    return sum(summation(i) if isinstance(i, list) else i for i in l)

if __name__ == "__main__":
    print(summation([1,[11,42,[8, 1], 4, [22,21]]]))
    print(summation([1,[11,42,[8, 1], [4,10,[75]], [22,21]]]))