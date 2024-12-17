#!C:/Python313/python.exe
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


print("Content-Type: text/html")
print()
with open("homepage.html", encoding='utf-8') as f:
    print(f.read(), end='')