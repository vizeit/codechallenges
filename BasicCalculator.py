def calculator(s):
    stack = []
    operator = ''
    while len(s):
        c = s.pop(0)
        if c not in ('+-*/()') and operator in (' +-'):
            d = int(c) if c.find('.')==-1 else float(c)
            stack.append(d) if operator in ('','+') else stack.append(-d)
        elif c not in ('+-*/()') and operator == '*':
            d = int(c) if c.find('.')==-1 else float(c)
            stack[-1] *= d
        elif c not in ('+-*/()') and operator == '/':
            d = int(c) if c.find('.')==-1 else float(c)
            stack[-1] =  stack[-1] / d if stack[-1] % d else stack[-1] // d
        elif c in ('+-*/'):
            operator = c
        elif c == '(':
            n = calculator(s) 
            if operator in (' +-'):
                stack.append(n) if operator in ('','+') else stack.append(-n)
            elif operator == '*':
                stack[-1] *= n
            elif operator == '/':
                stack[-1] =  stack[-1] / n if stack[-1] % n else stack[-1] // n
        elif c == ')':
            break
    return sum(stack) 

if __name__ == "__main__":
    print(calculator(list('1.1 * 2.2 * 3.3'.split())))
    print(calculator(list('1 + 2 * 3 / 2'.split())))
    print(calculator(list('( 1 + 2 ) * 6'.split())))
    print(calculator(list('( 2 * ( 1 + 2 ) ) * 3'.split())))


            