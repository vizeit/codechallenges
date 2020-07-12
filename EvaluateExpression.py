
def calc(expression):
    return _subcalc(list(expression))

def convertnum(c):
    return int(c) if c.find('.')==-1 else float(c)

def operation(c, stack, operator, unary):
    c = -c if unary == '-' else c
    if operator in (' +-'):
        stack.append(c) if operator in ('','+') else stack.append(-c)
    elif operator == '*':
        stack[-1] *= c
    elif operator == '/':
        stack[-1] =  stack[-1] / c if stack[-1] % c else stack[-1] // c

def _subcalc(s):
    stack = []
    unary, operand, operator = '', '', ''
    while len(s) >= 0:
        c = s.pop(0) if len(s) else '-1'
        if c == ' ': continue
        elif c in('.0123456789'): operand += c
        elif c in ('+-*/)') or c == '-1':
            if len(operand): 
                operation(convertnum(operand), stack, operator, unary)
                if c == '-1' or c == ')': break
                operator = c
                operand = ''
                unary = ''
            elif c == '-1' or c == ')': break
            elif len(stack) and len(operator)==0: operator = c  
            else: unary = c
        elif c == '(':
            n = _subcalc(s)
            operation(n, stack, operator, unary)
            operator = ''
            unary = ''
    return sum(stack)

if __name__ == "__main__":
    print(calc("-(5) * (-33 + -86 - -(88)) + (-100 + -((((-47 / -55)))) + 32)"))