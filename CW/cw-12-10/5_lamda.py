# Функціональні вирази, lambda.
lam2 = None
lam3 = None
y = 100
w = 1000

def create_lam2() :
    global lam2
    y = 200
    lam2 = lambda x : x + y # захват (замикання) здійснено для локальної змінної у


def create_lam3() :
    global lam3
    global w
    global y
    lam3 = lambda x : x + w


def oper( lam ) -> int :
    return lam( 10, 20 )

def main() :
    print( "+", oper( lambda x, y : x + y ) )
    print( "-", oper( lambda x, y : x - y ) )
    lam1 = lambda x : print(x)
    lam1( 10 )
    # IIFE Immediately Invoked Functional Expression
    ( lambda : print('IIFE') )()
    # CyMicHiCTb lambda Ta def
    print('*', oper( mul ) )
    create_lam2()
    y = 300
    print( lam2( 0 ) )
    print('--------')
    create_lam3()
    print(lam3(0))
    global w
    w = 2000
    print(lam3( 0 ) )


def mul(x, y):
    return x * y

if __name__ == '__main__': main()