import sys

# Define a function to check the text provided as a param.
def text_analyzer(string=None):
    # Repeat the input promt until a non-empty string is provided
    while string is None or string.strip() == "":
        text_analyzer(input("Please enter a string:  \n>>>> "))
        return
    if not isinstance(string, str):
        print("Error: Argument must be a string")
        return
    
    # Declare empty counters 
    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    # Sums characters 
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        else:
            punct_count += 1
    # Print results.
    print("The text contains", len(string), "characters")
    print("Upper-case characters :", upper_count)
    print("Lower-case characters :", lower_count)
    print("Punctuation characters : ", punct_count)
    print("Spaces :", space_count)

if __name__ == "__main__":
    # If arguments are more than one, print error.
    if len(sys.argv) > 2:
        print("Error: Too many arguments")
    # If arguments are 2 (program.py and "text", do text_analizer)
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    # If any text is provided, the program will ask you for it
    else:
        string = None
        while string is None or string.strip() == "":
            string = input("Please enter a string: \n>>>   ")
        text_analyzer(string)

