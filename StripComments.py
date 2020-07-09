def stripcomments(string,markers):
    rs = ''
    bcomment = False
    for c in string:
        if c in markers:
            bcomment = True
        if not bcomment:
            rs+=c
        elif bcomment and c == '\n':
            rs = rs.rstrip(' ')
            rs+='\n'
            bcomment = False
    return rs.rstrip(' ') 

if __name__ == "__main__":
    print(stripcomments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))