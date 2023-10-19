# tea = {"Alice", "Bob", "Charlie", "David", "Eve", "Fred","Kevin", "Linda"}
# coffee = {"Alice", "Bob","Gary", "Helen", "Ivan", "Jack", "Kevin", "Linda"}

# intersection_set = tea.intersection(coffee)
# print(intersection_set)

# only_tea = tea.difference(coffee)
# print(only_tea)

# only_coffee = coffee.difference(tea)
# print(only_coffee)

# union_set = tea.union(coffee)
# print(union_set)

# symmetric_difference_set = tea.symmetric_difference(coffee)
# print(symmetric_difference_set)

# To remove duplicates from a list, you can convert it to a set and then back to a list:
# mylist = ["apple", "banana", "cherry", "apple", "cherry","grape","orange"]
# mylist = set(mylist)
# print(mylist)
# mylist = list(mylist)
# print(mylist)


my_set = {1, 2, 3}
my_set.add(4) # Adding a single element to the set
my_set = frozenset(my_set)
my_set.update([5, 6, 7])

print(my_set)