
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.
def number_attributes(**kwargs):
    return len(kwargs)
print(number_attributes(fruit="apple", size="small", color="red")) 

# def produce_list(**kwargs):
#     count = 0
#     for key, value in kwargs.items():
#         key += kwargs
#     return count
# print(produce_list(fruit="apple", size="small", color="red"))
def produce_list(fruit, size, *args, **kwargs):
    count = 0
    for key, value in kwargs.items():
        count += 1
    return count
print(produce_list(fruit="apple", size="small", color="red"))

# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def list_attributes(**kwargs):
    attributes = []
    for key, value in kwargs.items():
        attributes.append(value)
    return attributes
print(list_attributes(fruit="apple", size="small", color="red"))

# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black

def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
describe_person("Ash", eye_color="brown", hair_color="black")
