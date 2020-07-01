def merge_the_tools(string, k):
    """
    Given a string and number k, split input string into k characters
    remove any repeating characters
    Sample Input
    AABCAAADA
    3   
    Sample Output
    AB
    CA
    AD
    """
    for i in range(0, len(string), k):
        t = ''
        for c in string[i:i+k]:
            if c not in t:
                t += c
        print(t)

if __name__ == "__main__":
    merge_the_tools('AABCAAADA', 3)