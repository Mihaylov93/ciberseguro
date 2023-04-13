import sys

# Define a function to check if a number is odd, even, or zero
def whois(number):
    if number == 0:
        return "Zero"
    elif number % 2 == 0:
        return "This number is Even."
    else:
        return "This number is Odd."

# Get the command-line arguments
args = sys.argv[1]

# Check if there are any arguments
if len(args) == 0:
    print("Usage: python3 program.py [number] ** No params provided")
# Check if there are too many arguments
elif len(args) > 1:
    print("Error. too many arguments.")
else:
    try:
        # Convert the argument to an integer
        number = int(args)
        
        # Check if the number is odd, even, or zero
        result = whois(number)
        
        # Print the result
        print(result)
    except (ValueError, IndexError):
        print("Error: Argument must be an integer")