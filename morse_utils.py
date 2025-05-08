MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

def encode_message(message):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in message if char.upper() in MORSE_CODE_DICT)

def decode_message(morse_code):
    inverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(inverse_dict.get(code, '') for code in morse_code.strip().split())

def get_random_word():
    import random
    words = ["HELLO", "WORLD", "PYTHON", "MORSE", "CODE", "TEST", "OPENAI", "QUIZ"]
    return random.choice(words)
