def create_http() :
    try :
        with open( "file2.txt", "w", encoding='utf-8' ) as file :
            file.write( "Host: localhost\r\n" )
            file.write( "Connection: close\r\n" )
            file.write( "Content-Type: text/html\r\n" )
            file.write( "Content-Length: 100500\r\n" )
            file.write( "Accept: *.* \r\n" )
            file.write( "\r\n" )
            file.write( "<html></html>" )
    except OSError as err :
        print( "Error reading file: ", err )

def parse_http_imp() -> dict | None :
    d = {}
    try :
        with open( "file2.txt", "r", encoding='utf-8' ) as file :
            for line in file :
                if ':' in line :
                    k, v = line.split(':')
                    d[k] = v
        return d
    except OSError as err :
        print( "Error reading file: ", err )
        return None


def main() :
    #create_http()
    for k, v in parse_http_imp().items():
        print(k, v)
    print('----------')
    d = {}
    print( type(d) )
    d["a"] = 1
    d["b"] = 2
    print( d )
    d2 = {k: str(k)
        for k in range(10)}


if __name__ == "__main__" : main()