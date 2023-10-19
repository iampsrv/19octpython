def greet(name = "Pranjal", greeting="Hello"):
    print(greeting, name)

def add(*args):
    result = 0
    for number in args:
        result += number
    return result

def dollartoeuro(dollar):
    euro = dollar * 0.94
    return euro