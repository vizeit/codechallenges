from collections import Counter
def no_duplicate_letters(phrase):
    """
    Given a common phrase, return False if any individual word in the phrase contains duplicate letters. 
    Return True otherwise.
    Letter matches are case-insensitive.
    """
    for w in phrase.split():
        if any(c > 1 for _,c in Counter(w.lower()).items()):
            return False
    return True

if __name__ == "__main__":
    print(no_duplicate_letters("Fortune favours the bold."))
    print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
    print(no_duplicate_letters("Look before you leap."))
    print(no_duplicate_letters("An apple a day keeps the doctor away."))