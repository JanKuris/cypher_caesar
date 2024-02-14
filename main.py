alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3' '4', '5', '6', '7', ' 8', '9', "!", '@', "#", "$", "%", "_", " ", ")", "(", "*", ",", "."]
# numbers = ['0', '1', '2', '3' '4', '5', '6', '7', ' 8', '9']
# symbols = ["!", '@', "#", "$", "%", "_", " ", ")", "(", "*", ",", "."]

def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:
            access_to_list = alphabet.index(character)
            new_position = access_to_list + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += character
    print(f"The {cipher_direction} text is {end_text}")

ceasar_end = False
while not ceasar_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 25:
        shift = shift % 25

    ceasar(start_text = text, shift_amount = shift, cipher_direction = direction)
    
    user_continue = input("If you want start again type 'yes'.\n").lower()
    if user_continue == "yes":
        ceasar(start_text = text, shift_amount = shift, cipher_direction = direction) 
    else:
        print("Bye")
        break 


