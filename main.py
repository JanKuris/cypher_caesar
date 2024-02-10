alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
   cipher_text = ""
   for letter in plain_text: 
      access_list = alphabet.index(letter)
      cipher_letter = access_list + shift_amount
      if access_list >= 17:
         # cipher_letter = access_list + shift_amount
         if cipher_letter >= 25: 
            cipher_letter = (24 - access_list) + shift_amount
      new_letter = alphabet[cipher_letter]
      cipher_text += new_letter
   print(cipher_text)


print(encrypt(plain_text = text, shift_amount = shift))





