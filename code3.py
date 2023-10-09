# Code3:
# Objective: To identify and fix errors in a Python program that reads and writes to a file.
def read_and_write_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        with open(filename, 'w') as file:
            file.write(content.upper())
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()

# submit the corrected code with comments explaining the issues they found and the solutions they implemented.


# ANSWER:
# _______________________EXPLANATION___________________________
# The Python program you’ve provided is correct and doesn’t have any errors. It’s a simple program to read a file, convert its content to uppercase, and write it back to the same file. Here’s how it works:

# The read_and_write_file(filename) function takes a filename as an argument.
# It tries to open the file in read mode and reads its content.
# Then it opens the file in write mode and writes the content back to the file after converting it to uppercase using the upper() method.
# If the file is processed successfully, it prints a success message. If an error occurs (for example, if the file does not exist), it catches the exception and prints an error message.
# The main() function calls read_and_write_file(filename) with “sample.txt” as the argument.
# The line if __name__ == "__main__": main() ensures that main() is called when the script is run directly, but not when its functions are imported into another script.
# So, if you run this program with a file named “sample.txt” in the same directory, it will convert all text in “sample.txt” to uppercase. If “sample.txt” does not exist or cannot be opened, it will print an error message.
#use The relative path of the text file instead if it resides in other directory as shown.

def read_and_write_file(filename):
    try:
        # Open the file in read mode and read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Open the file in write mode and write the uppercase content back to it if the file exist in same directory
        with open(filename, 'w') as file:
            file.write(content.upper())
        
        # Print a success message
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        # If an error occurs (e.g., the file does not exist), print an error message
        print(f"An error occurred: {str(e)}")

def main():
    # Call read_and_write_file() with "sample.txt" as the argument
    filename = "sample.txt"
    read_and_write_file(filename)

# Ensure that main() is called when the script is run directly
if __name__ == "__main__":
    main()
