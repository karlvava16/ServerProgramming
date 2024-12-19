#!C:/Python313/python.exe

# Диспетчер доступу - модуль програми, через який проходять усі запити.
# Запити, що не проходять через нього не повинні обслуговуватися

import codecs
import sys

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

def send_error(code=400, phrase="Bad Request", explain=None):
    print(f"Status: {code} {phrase}")
    print("Content-Type: text/plain; charset=utf-8")
    print()
    print(explain if explain else phrase)
    exit()

def send_file( filename:str ) :
    print( "Content-Type: text/html; charset=utf-8" )
    print()
    with open( filename, encoding="utf-8" ) as file :
        print( file.read() )
    exit()

import os
envs = {
    k: v for k, v in os.environ.items()
    if k in ('REQUEST_METHOD', 'QUERY_STRING', 'REQUEST_URI')
}
path = envs['REQUEST_URI']
if '?' in path:
    path = path[:path.index('?')]
if path.startswith( '/' ) :
    path = path[1:]

# Аналізувати path, здійснюємо маршрутизацію
if path == '':
    send_file("homepage.html")
else:
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(path)

