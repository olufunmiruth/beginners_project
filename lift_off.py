"""
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

num_constant = 10  # assigns the number of values
print("Let the countdown begin")
num = num_constant  # equates the variable to the constant so any number can work
print(str(num))
# returns the starting value
for i in range(num_constant):  # loops the numbers from the num_constant.
    num -= 1
    # this calculates the values by subtracting 1 from the num_constant each time it goes through the loop
    print(str(num))  # prints result after converting to a string
print("Liftoff!!!")
