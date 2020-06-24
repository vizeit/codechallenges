def uncensor(txt, vowels):
    """
    Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. 
    Luckily, I've been able to find the vowels that were removed.
    Given a censored string and a string of the censored vowels, 
    return the original uncensored string.
    Notes
    The vowels are given in the correct order.
    The number of vowels will match the number of * characters in the censored string
    """
    vl = list(vowels[::-1])
    return ''.join(vl.pop() if c == '*' else c for c in txt)

if __name__ == "__main__":
    print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
    print(uncensor("abcd", ""))
    print(uncensor("*PP*RC*S*", "UEAE"))