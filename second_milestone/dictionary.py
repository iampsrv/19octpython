# # We can use a dictionary to store information about a student.
# student = {
#     "name": "John",
#     "age": 25,
#     "courses": ["Math", "CompSci"]
# }
# student["name"] = "Pranjal"
# student["city"] = "New York"
# print(student)
# print(student.keys())

# # print(student)    
# # import json
# # # convert this dictionary to a JSON string
# # student_json = json.dumps(student)
# # print(student_json)

# # print(type(student_json))

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}
print(merged_dict)