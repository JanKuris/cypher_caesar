alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    # if letter is special sign or space
    if not letter in alphabet:
      end_text += letter
    else:
      idx = alphabet.index(letter)
      shifted_idx = ((idx + shift_amount) % 26)
      end_text += alphabet[shifted_idx]    
  print(f"Here's the {cipher_direction}d result: '{end_text}'")
 
 
#Hint: Try creating a new function that calls itself if they type 'yes'.
def call_ceasar_again():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))
 
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
 
asking_again = True
while asking_again == True:
  call_ceasar_again()
  question = input("Do you want to ask again? - yes/no: ")
  if question == 'no':
    asking_again = False
    print("Goodbye!")