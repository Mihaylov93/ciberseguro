import sys

def reverse_swap(string):
    # Reverse the string
    reversed_string = string[::-1]
    
    # Swap the case of the string
    swapped_string = reversed_string.swapcase()
    
    return swapped_string

# Get the command-line arguments
args = sys.argv[1:]

if len(args) == 0:
    print("Usage: python3 program.py [string] ** No params provided **")
else:
    # Merge the arguments into a single string
    string = " ".join(args)
    
    # Reverse and swap the case of the string
    result = reverse_swap(string)
    
    # Print the result
    print(result)