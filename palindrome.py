import sys
if len(sys.argv) == 2:
    text = sys.argv[1] 
    print("User provided input:")
else:
    print("No command-line input provided. Using manual input:")
    text = input("Enter a string: ")  
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")