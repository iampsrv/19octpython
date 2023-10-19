# # Give me example for all Arithmetic Operators

# # Addition
# print(2 + 3)

# # Subtraction
# print(2 - 3)

# # Multiplication
# print(2 * 3)

# # Division
# print(2 / 3)

# # Floor Division
# print(2 // 3)

# # Modulus
# print(25 % 3)

# # Exponentiation
# print(2 ** 3)

# number_of_visits=19
# if number_of_visits>10 and number_of_visits<20:
#     print("You will get 20% discount")
# elif number_of_visits<10:
#     print("You will get 5% discount")
# elif number_of_visits>20:
#     print("You will get 30% discount")
# else:
#     print("You will get 10% discount")

# age =-1
# if age>18:
#     print("You are eligible to vote")
# elif age<18 and age==18:
#     print("You are not eligible to vote")
# else:
#     print("Invalid age")

# a = 10
# b = 20
# if a!=b:
#     print("a is not equal to b")
# else:
#     print("a is equal to b")

# a = 20

# # a = a + 1
# a *= 1
# print(a)

# mynumber = [1,2,3,4,5,6,7,8,9,10] #list of numbers from 1 to 10
# studentnames = ['Alice','Bob','Charlie','David','Eve','Fred','Ginny','Harriet','Ileana','Joseph','Pranjal'] #list of names of students

# if 'Pranjal' in studentnames:
#     print("Pranjal is present in the class")
# else:
#     print("Pranjal is not present in the class")

# a = [1,2,3]
# b = a
# c= [1,2,3]
# print(id(a))
# print(id(b))
# if a is not c:
#     print("a and c are not same")
# else:
#     print("a and c are same")

# give me one example for bitwise operator to check even odd and calculate its execution time


# a = 10
# b = 20
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is less than b")
# else:
#     print("a is equal to b")



import time
 
start = time.time()
 
a=int(input("Please Enter a Number : ")) 
# if(a&1==1): 
if(a%2==1):
    print("This Number is Odd")
else:
    print("This Number is Even")
end = time.time()
 
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
