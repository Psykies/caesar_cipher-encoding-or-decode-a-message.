alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while (direction != "encode") and (direction != "decode"):
  print("there is only two ways to do this either encode or decode")
  direction = input("Type 'encode' to encrypt, type 'decode' to   decrypt:\n")
  
text = input("Type your word:\n").lower()
shift = int(input("Type the shift number less than 27:\n"))
while shift > 26:
  shift = int(input("Type the shift number less than 27:\n"))

  
#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
   #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5 here the shift number can only be up to 26 since 26 alphabet
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"


def encrypt (plain_text, shift_number):
  cipher_text = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_number
      new_letter = alphabet[new_position]
      cipher_text += new_letter 
    else:
      cipher_text += letter
      

  print(f"The encoded text is {cipher_text}")  
  



#decoding the message
def decrypt (plain_text, shift_number):
  cipher_text = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position - shift_number
      new_letter = alphabet[new_position]
      cipher_text += new_letter 
    else:
      cipher_text += letter
  print(f"The encoded text is {cipher_text}")

#logical oeprator to encode or decode
if direction == "encode":
  encrypt (plain_text=text,shift_number =shift)
else:
  decrypt (plain_text=text,shift_number =shift)
  