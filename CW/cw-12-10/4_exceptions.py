from typing import final


def throws() :
    raise TypeError

def mem() :
    try:
        return 10
    finally:
        print("Done return mem")


def main() :
    print( "Before throw" )
    try :
        throws ()
    except TypeError :
        print( "TypeError caught")
    except ValueError as err :
        print( "ValueError", err )
    except :
        print("Unknown error")
    else:
        print( "No exception raised")   # блок виконується якщо try завершився успішно
    finally:
        print( "Finally" )
    print("After finally")
    print(mem())


if __name__ == "__main__" : main()