from itertools import accumulate

def valid_parentheses(string):
    """
    Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
    Examples

    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true
    """
    l = list(accumulate(map(int, map(lambda x: '1' if x == '(' else '-1' if x == ')' else 0, string))))
    return True if len(string) == 0 else all(i>=0 for i in l) and l[-1] == 0

if __name__ == "__main__":
    print(valid_parentheses("()"))
    print(valid_parentheses(")(()))"))
    print(valid_parentheses("(())((()())())"))