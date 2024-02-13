alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3' '4', '5', '6', '7', ' 8', '9']
symbols = ["!", '@', "#", "$", "%", "_", " ", ")", "(", "*"]


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        access_to_list = alphabet.index(letter)
        new_position = access_to_list + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")

if shift >= 25:
    shift = shift % 25
   
    
ceasar(start_text = text, shift_amount = shift, cipher_direction = direction) 


