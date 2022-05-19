# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
# Examples(Operator, value1, value2) --> output

# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

# my answer
def basic_op(operator, value1, value2):
    #your code here
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# other answers
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))





print(basic_op('+', 4, 66))
print(basic_op('-', 4, 66))
print(basic_op('*', 4, 66))
print(basic_op('/', 4, 66))
print(basic_op('**', 4, 66))