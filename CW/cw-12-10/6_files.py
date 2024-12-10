# Робота з файлами

def create_file() -> None:
    try:
        file = open('file.txt', 'w', encoding='utf-8')
        file.write('Latin content\r\n')
        file.write('Кирилічний контент')
    except OSError as err:
        print('Error writing file', err)
    else:
        file.flush()
        print('Write file OK')
    finally:
        file.close()

def read_file() -> None :
    try :
        with open( "file.txt", "r", encoding='utf-8') as file :
            print(file.read())
    except OSError as err:
        print('Error reading file', err)

def read_file2() -> None :
    try :
        with open( "file.txt", "r", encoding='utf-8') as file :
           for line in file :
               print(line)
    except OSError as err:
        print('Error reading file', err)

def main():
    create_file()
    read_file()

if __name__ == '__main__': main()
