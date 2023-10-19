# def greet():
#     print("Hello, world!")

# greet()
# greet()
# greet()

def dollartoeuro(dollar):
    euro = dollar * 0.94
    return euro

# valueineuro = dollartoeuro(100)
# print(valueineuro)
# print(dollartoeuro(100))
# print(dollartoeuro(948))

# dollar = 100
# euro = dollar * 0.94
# print(euro)

# dollar = 948
# print(euro)


# def add(a, b,c):
#     return a + b + c
# def add(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result

# print(add(1, 2, 3,4,5,6,7,8,9,10))

def greet(name = "Pranjal", greeting="Hello"):
    print(greeting, name)
    
greet()
greet("Bob")
greet("Bob", "Welcome")