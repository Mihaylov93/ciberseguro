

import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

def encode_morse(s):
    encoded = []
    for c in s.upper():
        if c in MORSE_CODE_DICT:
            encoded.append(MORSE_CODE_DICT[c])
        else:
            return("ERROR")
        
    return ' '.join(encoded)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python morse.py <string>')
        sys.exit(1)
    s = ' '.join(sys.argv[1:])
    encoded = encode_morse(s)
    print(encoded)