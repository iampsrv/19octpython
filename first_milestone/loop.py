number_of_lives = 3

for life in range(number_of_lives):
    print("Not killed by an enemy")
    print("You have " + str(number_of_lives - life) + " lives left")
    print("killed by an enemy")