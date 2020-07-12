def convertnum(c):
    return int(c) if c.find('.')==-1 else float(c)

def operation(c, operator, stack):
    if operator in (' +-'):
        stack.append(c) if operator in ('','+') else stack.append(-c)
    elif operator == '*':
        stack[-1] *= c
    elif operator == '/':
        stack[-1] =  stack[-1] / c if stack[-1] % c else stack[-1] // c

def calculator(s):
    if len(s) == 0: raise Exception('Invalid Expression')
    stack = []
    operator = ''
    ts = ''
    while len(s) >= 0:
        c = s.pop(0) if len(s) else '-1'
        if c == ' ': continue
        elif c in('.0123456789'): ts += c
        elif c in ('+-*/') or (c == '-1' and len(s) == 0) or c == ')':
            if (len(ts)==0 and len(stack)==0) or (len(ts)==0 and len(operator) and operator in '+-*/' and c in '+-*/' ): 
                raise Exception('Invalid Expression')
            elif len(ts): operation(convertnum(ts), operator, stack)
            if c == '-1' or c == ')': break
            else: operator = c
            ts = ''
        elif c == '(':
            n = calculator(s) 
            operation(n, operator, stack)
        elif c == ')':
            break
    return sum(stack) 

if __name__ == "__main__":
    try:
        print(calculator(list('1+1')))
        print(calculator(list('1.1*2.2* 3.3')))
        print(calculator(list('1+2*3/2')))
        print(calculator(list('(1+2)*6')))
        print(calculator(list('(2*(1+2))*3')))
        print(calculator(list('(2*((1+2)*(2+3)))*2')))
        print(calculator(list('1*/1')))
    except Exception as e:
        print(e)


            