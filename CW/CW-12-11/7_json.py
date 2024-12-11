# робота з JSON
import json

str = '''{
    "str": "String value",
    "digital": 123,
    "float": 123.456,
    "bool": true,
    "obj": {
    "x": 10,
    "y": 20
    },
    "arr": [1, 2, 3, 4, 5],
    "null": null
}'''

j = json.loads( str )
print( j, type(j) )