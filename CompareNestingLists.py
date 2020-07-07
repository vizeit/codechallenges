def comparenestinglists(ls, ld):
    if isinstance(ls, list) and isinstance(ld, list) and len(ls) == len(ld):
        for l1, l2 in zip(ls, ld):
            if not comparenestinglists(l1, l2):
                return False
            else:
                return True
    else:
        return not isinstance(ls, list) and not isinstance(ld, list)

if __name__ == "__main__":
    print(comparenestinglists([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]))
    print(comparenestinglists([[3, 0], 3, 1, [4, 1, 4], [2, 0, 4], [3, 2, 1], [4, 0]]
, [[0, 2], [4, 1, 3], [3, 0, 4, 1], [0, 1, 3], [4, 4, 1], [2], [0, 3, 1, 2], [2, 3], [0, 2, 2], 1, [0], [2, 1, 1, 0], 0, 1, [2, 1, 3], [3, 1, 2, 2]]))