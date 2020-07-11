def convertnum(c):
    return int(c) if c.find('.')==-1 else float(c)

def parseexpression(s):
    rs, i, ts = [], 0, ''
    for c in s:
        if c == ' ': continue
        elif c in('.0123456789'): ts += c
        elif c in ('+-*/()'):
            if len(ts): rs.append(convertnum(ts))
            if len(rs) and isinstance(rs[-1],str) and ((rs[-1] in ('+-*/') and c in('+-*/')) or (rs[-1] == '(' and c == ')')):
                raise Exception('Invalid expression')
            rs.append(c)
            ts = ''
        else: raise Exception('Invalid expression')
    if len(ts): rs.append(convertnum(ts))
    return rs

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
    while len(s):
        c = s.pop(0)
        if isinstance(c, int) or isinstance(c, float):
            operation(c, operator, stack)
        elif c in ('+-*/'):
            operator = c
        elif c == '(':
            n = calculator(s) 
            operation(n, operator, stack)
        elif c == ')':
            break
    return sum(stack) 

if __name__ == "__main__":
    try:
        print(calculator(parseexpression('1.1*2.2* 3.3')))
        print(calculator(parseexpression('1+2*3/2')))
        print(calculator(parseexpression('(1+2)*6')))
        print(calculator(parseexpression('(2*(1+2))*3')))
        print(calculator(parseexpression('2*((1+2)*(2+3))*2')))
    except Exception as e:
        print(e)


            