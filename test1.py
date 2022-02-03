a = int(input("please input 1st number"))
b = int(input("please input 2nd number"))
x = input("please input the operator sign")


def sum(a, b):
    return a + b


def division(a, b):
    return a/b


def multiplication(a, b):
    return a*b


def minus(a, b):
    return a - b

if (x == '+'):
    print(sum(a, b))
elif (x == '-'):
    print(minus(a, b))
elif (x == '*'):
    print(multiplication(a, b))
elif (x == '/'):
    print(division(a, b))