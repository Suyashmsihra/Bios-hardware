def text_to_morse(text):

    morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                  'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                  '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '}


    text = text.upper()


    morse_code = ''
    for char in text:
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
        else:
            morse_code += char

    return morse_code.strip()


# Example usage
text = "I am intrested to get into bios hardware"
morse_code = text_to_morse(text)
print("Input Text: ", text)
print("Morse Code: ", morse_code)
