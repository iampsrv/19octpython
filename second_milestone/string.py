# age = "26"

# print(type(age))

# age = int(age)
# print(type(age))

# age = str(age)
# print(type(age))


# text = "Hello, World!"
# new_text = text.replace("World", "Python")
# print(new_text)

# a = "Hello"
# b = "     Hello"

# name = "Alice"
# age = 25
# message = f"My name is {name} and I'm {age} years old."
# print(message)

text = "P7y8t9h6o4n"
digits = ''.join(filter(str.isdigit, text))
letters = ''.join(filter(str.isalpha, text))
print(digits) # Output: "78964"
print(letters) # Output: "Python"