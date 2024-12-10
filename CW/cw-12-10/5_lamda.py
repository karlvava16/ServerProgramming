# Функціональні вирази, lambda.
def oper(lam) -> int:
    return lam(10, 20)

def main():
    print("+", oper(lambda x, y: x + y))
    print("-", oper(lambda x, y: x - y))
    lam1 = lambda x: print(x)
    lam1(10)
    # IIFE Immediately Invoked Functional Expression
    ( lambda: print('IIFE') )()
    print('*', oper(mul))


def mul(x, y):
    return x * y

if __name__ == '__main__': main()