# prgrm to check if two strings are balanced

"""
the func below adds the count of each character in the string 
to the dictionary (ig you can call it a hash table)
"""


def add_to_dict(str, dict):
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1


"""
the func below checks if the two strings are balanced 
by balancing the hash tables
(I've used guard clauses to reduce the nesting)
"""


def check_balance(str1, str2):
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return True
    dict1 = {}
    dict2 = {}
    add_to_dict(str1, dict1)
    add_to_dict(str2, dict2)
    if dict1 == dict2:
        return True
    return False


# test cases
print("Prewritten test cases:")
print('"abc" - "cba"', check_balance("abc", "cba"))  # True
print('"abc" - "cbd"', check_balance("abc", "cbd"))  # False
print('"abc" - "cb"', check_balance("abc", "cb"), end="\n\n")  # False

# user input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("The strings are balanced") if check_balance(str1, str2) else print(
    "The strings are not balanced"
)
