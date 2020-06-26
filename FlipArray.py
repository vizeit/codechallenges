import numpy
def flip_list(lst):
    """
    Create a function that flips a horizontal list into a vertical list, 
    and a vertical list into a horizontal list.
    In other words, take an 1 x n list (1 row + n columns) and flip it into 
    a n x 1 list (n rows and 1 column), and vice versa.
    """
    return numpy.reshape(lst, (numpy.array(lst).shape[0],1)) if len(numpy.array(lst).shape) == 1 else numpy.reshape(lst, (numpy.array(lst).shape[0],))

if __name__ == "__main__":
    print(flip_list([1, 2, 3, 4]))
    print(flip_list([[5], [6], [9]]))
    print(flip_list([]))