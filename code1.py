# Code 1:
# Objective: To identify and fix errors in a Python program that manipulates strings.
def reverse_string(s):
    reversed = ""
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]
    return reversed

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()

# _______________________EXPLANATION___________________________
# The Python program you’ve provided is correct and doesn’t have any errors. It’s a simple program to reverse a string. Here’s how it works:

# The reverse_string(s) function takes a string s as an argument. It initializes an empty string reversed.
# Then it iterates over the string s in reverse order (from the last character to the first) using the range(len(s) - 1, -1, -1) construct.
# In each iteration, it adds the current character to the reversed string.
# After all characters are processed, it returns the reversed string which is the reverse of the input string s.
# The main() function defines a string “Hello, world!”, reverses it using the reverse_string(input_string) function, and prints the reversed string.
# The line if __name__ == "__main__": main() ensures that main() is called when the script is run directly, but not when its functions are imported into another script.
# So, if you run this program, it will print: “Reversed string: !dlrow ,olleH”. This is the reverse of “Hello, world!”.


# ****************************************************************************************************************


