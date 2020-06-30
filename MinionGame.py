def minion_game(string):
    """
    Kevin and Stuart want to play the 'The Minion Game'.
    Game Rules
    Both players are given the same string,
    Both players have to make substrings using the letters of the string
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.
    Scoring
    A player gets +1 point for each occurrence of the substring in the string
    For Example:
    String = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
    Your task is to determine the winner of the game and their score.
    Input Format
    A single line of input containing the string
    Note: The string will contain only uppercase letters:
    Output Format
    Print one line: the name of the winner and their 
    score separated by a space.
    If the game is a draw, print Draw.
    """
    s, k = 0, 0
    for i in range(len(string)):
        if string[i].lower() in 'aeiou':
            k += (len(string)-i)
        else:
            s += (len(string)-i)
    return 'Draw' if s == k else f'Stuart {s}' if s > k else f'Kevin {k}'

if __name__ == "__main__":
    print(minion_game('BANANA'))
    print(minion_game('ANACONDA'))