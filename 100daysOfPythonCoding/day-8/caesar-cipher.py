letters = ['a', 'b', 'c', 'd','e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continueProgram = True


def askInput():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    if shift > 25:
        shift = shift%26
    return (direction, text, shift)

def caesar(text, shift, direction):
    encoded_decoded_str = ""
    for char in text:
        char_pos = letters.index(char)
        if direction == "encode":
            encode_decode_pos = char_pos+shift
        elif direction == "decode":
            encode_decode_pos = char_pos-shift
        else:
            print ("Incorrect input. Plrease try again. \n")
            break
        if encode_decode_pos > 25:
            encode_decode_pos = encode_decode_pos-26
        encoded_decoded_str = encoded_decoded_str + letters[encode_decode_pos]
    return encoded_decoded_str




def ask_for_continue():
    return input("DO you want to continue for encode / decode your message? Type yes or no: ").lower()

while continueProgram:
    direction, text, shift = askInput()
    print(f"Your Message is : {caesar(text, shift, direction)} \n")
    IsContinue = ask_for_continue()
    if IsContinue == "yes":
        continueProgram = True
    elif IsContinue == "no":
        print("Good Bye...")
        continueProgram = False
    else:
        print ("incorrect input. Plrease try again. \n")
        #IsContinue = ask_for_continue()
    

