# Code2:
# Objective: To identify and fix errors in a Python program that validates user input.

def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and age >= 18:
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()


# ANSWER:
# _______________________EXPLANATION___________________________

#The issue with your code is in the get_age() function. The input() function in Python always returns a string, and you’re comparing a string with an integer in the condition age >= 18. This will result in a TypeError.
#   HERE MAINLY  -------if age.isnumeric() and age >= 18:-------
# To fix this, you should convert the input to an integer before comparing it with 18. However, before doing that, you should check if the input is numeric to avoid a ValueError when trying to convert a non-numeric string to an integer. Here’s the corrected code:


def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18:
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()


# *********************************************************************************************************
