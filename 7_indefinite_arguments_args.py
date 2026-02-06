def tea_order(customer_name, tea_type, *args, **kwargs):
        print(customer_name, "ordered a", tea_type, "tea.")
        for key, value in kwargs.items():
                print(" - Add:", key, "=", value)

print(tea_order("Alice", "chamomile"))
print(tea_order("Bob", "earl grey", milk = "whole milk", sweetener = "2 sugars"))
print(tea_order("Charlie", "green", lemon = "2 slices", honey = "1 spoon", ice = "yes"))

# -------------------------------------------
# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

def sum_squares(*args):
    sum = 0 #Initialize sum to 0
    for number in args: #Iterate through each argument
        sum += number ** 2 #square the number and add to sum
    return sum 
print(sum_squares(1, 2, 3))  # Output: 14

# -------------------------------------------
# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

def absolute_sum(*args):
    total = 0  # Initialize through total to 0
    for num in args:  # Iterate through each argument
        total += abs(num)  # Add the absolute value of the number to total
        # first time through: total = 0 + abs(-1) = 1
        # second time through: total = 1 + abs(-2) = 3
        # third time through: total = 3 + abs(3) = 6
    return total
print(absolute_sum(-1, -2, 3))  # Output: 6

# -------------------------------------------
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"

def personal_numbers(name, *args):
    sum_numbers = sum(args)  # Calculate the sum of the numbers in args
    return f"{name}, the sum of your numbers is {sum_numbers}"
print(personal_numbers("David", 10, 20, 30))  # Output: "David, the sum of your numbers is 60"