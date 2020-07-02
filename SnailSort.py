def snailsort(arr):
    """
    Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
    array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]
    For better understanding, please follow the numbers 
    of the next array consecutively:

    array = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    snail(array) #=> [1,2,3,4,5,6,7,8,9]
    """
    if arr[0] == 0: #empty matrix condition
        return []
    r, c = 0, -1
    rs = []
    #direction: 1 - right, 2 - down, 3 - left, 4 - up
    direction = 1 #initially right direction
    while len(rs) < len(arr)*len(arr):
        while (direction == 1 and c < len(arr)-1) or (direction == 3 and c > 0) or (direction == 2 and r < len(arr)-1) or (direction == 4 and r > 0):
            if direction == 1 and arr[r][c+1] != float('inf'):
                c += 1
            elif direction == 2 and arr[r+1][c] != float('inf'):
                r += 1
            elif direction == 3 and arr[r][c-1] != float('inf'):
                c -= 1
            elif direction == 4 and arr[r-1][c] != float('inf'):
                r -= 1
            else:
                break #change direction if value already seen
            rs.append(arr[r][c])
            arr[r][c] = float('inf')
        direction = 1 if direction == 4 else direction + 1
    return rs

if __name__ == "__main__":
    array = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]
    print(snailsort(array))
