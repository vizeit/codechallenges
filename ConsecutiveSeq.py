def consecutive_combo(lst1, lst2):
    """
    Write a function that returns True if two lists, when combined, form a consecutive sequence.
        The input lists will have unique values.
        The input lists can be in any order.
        A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
    """
    l = sorted(lst1+lst2)
    if l:
        if l[0] + len(l) - 1 == l[-1]:
            return True
    return False

if __name__ == "__main__":
    print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
    print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
    print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
    print(consecutive_combo([44, 46], [45]))