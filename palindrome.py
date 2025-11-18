import sys

try:
    # If argument is given, use it
    if len(sys.argv) >= 2:
        text = sys.argv[1]
        print("User provided input:")
    else:
        # Try manual input
        print("No command-line input provided. Using manual input:")
        text = input("Enter a string: ")

except EOFError:
    print("No input available. Setting default value.")
    text = "" 
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")