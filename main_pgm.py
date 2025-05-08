from morse_utils import encode_message, decode_message, get_random_word

def encode_quiz():
    word = get_random_word()
    print(f"\nEncode this text into Morse code: {word}")
    
    user_input = input("Your answer: ").strip()
    correct_answer = encode_message(word)
    
    if user_input == correct_answer:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect!\nThe correct Morse code is: {correct_answer}")

def decode_quiz():
    word = get_random_word()
    morse_code = encode_message(word)
    
    print(f"\nDecode this Morse code into text: {morse_code}")
    
    user_input = input("Your answer: ").strip().upper()
    
    if user_input == word:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect!\nThe correct text is: {word}")

def main():
    print("=== Welcome to Morse Code Station ===")
    
    while True:
        choice = input("\nSelect mode: (E)ncode, (D)ecode, (Q)uit: ").strip().upper()
        
        if choice == 'E':
            encode_quiz()
        elif choice == 'D':
            decode_quiz()
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter E, D, or Q.")

if __name__ == "__main__":
    main()
