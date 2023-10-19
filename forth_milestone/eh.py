while(1):
    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter a number: "))
        a=x/y
        print(a)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        
    