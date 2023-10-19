my_list= [1,2,3,4,5,6,7,8,9,10]

# my_list1 = list(range(1, 5))

# print(my_list1)

# for i in my_list:
#     print(i)

fruits = ['apple', 'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# print(fruits[0])
# fruits[0] = 'pear'
# print(fruits[0])
# print(fruits)

# fruits.remove('banana') # Removing a specific element
# del fruits[1] # Removing element at index 0
# fruits.pop()
# print(len(fruits))

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 =[7, 8, 9]
# concatenated_list = list1 + list2 + list3
# print(concatenated_list)


# count = fruits.count("apple") # Counting occurrences of element 2
# print(count)

# fruits.reverse()
# print(fruits)

# my_list = [1, 2, 3]
# a, b, c = my_list # Unpacking the list into separate variables
# print(a, b, c)

marks = [80, 90, 70, 60, 95]
average = sum(marks) / len(marks)
print(average)
print(type(marks))
# print(min(marks))
# print(max(marks))
marks = tuple(marks)
print(type(marks))
marks[3] = 100

average = sum(marks) / len(marks)
print(average)

