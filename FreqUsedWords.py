from collections import defaultdict
from string import punctuation
def frequsedwords(s):
    d = defaultdict(int)
    s = s.translate({ord(c):ord(' ') for c in punctuation if c != "'"})
    for w in s.split():
        if len(w.strip(" ")) and w.replace("'","").isalpha():
            d[w.strip(' ').lower()]+=1
    return sorted(d, key=lambda x: d[x],reverse=True)[:3]

if __name__ == "__main__":
    print(frequsedwords("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."))
    print(frequsedwords("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
    print(frequsedwords("  //wont won't won't"))
    print(frequsedwords("  , e   .. "))