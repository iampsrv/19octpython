num = [1,2,3,4,5,6,7,8,9,10]

# even = []

# for n in num:
#     if n % 2 == 0:
#         even.append(n)
# print(even)

# print([n for n in num if n % 2 != 0])


square_dict = {x: x ** 2 for x in num if x % 2 != 0}
print(square_dict)