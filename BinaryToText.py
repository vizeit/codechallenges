def binary_to_text(n):
    """
    Create a function that takes a binary string and returns the text. The eight bits on the binary string represent 1 character on the ASCII table. For further info, check out the resource tab.
    Examples
    binary_to_text("01101110011011110110010001100101") ➞ "node"
    binary_to_text('0111001001100101011000010110001101110100') ➞ "react"
    binary_to_text("011100000111100101110100011010000110111101101110") ➞ "python"

    Notes
    Inputs are all valid strings.
    """
    return ''.join(chr(int(n[i:i+8],2)) for i in range(0,len(n),8))

if __name__ == "__main__":
    print(binary_to_text("01101110011011110110010001100101"))
    print(binary_to_text('0111001001100101011000010110001101110100'))
    print(binary_to_text("011100000111100101110100011010000110111101101110"))
