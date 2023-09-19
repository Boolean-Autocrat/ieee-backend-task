# prgrm to check if two strings are balanced
# (all chars in s1 are in s2)


def check_balance(str1, str2):
    for char in str1:
        if char not in str2:
            return False
        else:
            str2 = str2.replace(char, "", 1)
    return True


# test cases
print("Prewritten test cases:")
print('"abc" - "cba"', check_balance("abc", "cba"))  # True
print('"abc" - "cbd"', check_balance("abc", "cbd"))  # False
print('"abc" - "cb"', check_balance("abc", "cb"), end="\n\n")  # False

# user input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(
    "The strings are balanced.\nAll character in the first string are present in the second string!"
) if check_balance(str1, str2) else print(
    "The strings are not balanced.\nAll characters in the first string are not present in the second string."
)
