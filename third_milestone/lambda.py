my_list = [1,2,3,4,5,6,7,8,9,10]

# even = list(filter(lambda x: x % 2 == 0, my_list))
# print(even)

# map
my_list = [1,2,3,4,5,6,7,8,9,10]

def multiply_by2(item):
    return item * 2

# print(list(map(multiply_by2, my_list)))

mynewlist=[]
for n in my_list:
    mynewlist.append(multiply_by2(n))

print(mynewlist)

