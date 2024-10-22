# Define the alphabet as a list of letters
from pydoc import plain

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Get user input for encoding/decoding
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()  # Convert input to lowercase
shift = int(input("Type the shift number:\n"))  # Get the shift value as an integer


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""  # Initialize an empty string for the encrypted message

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
    for letter in plain_text:  # Iterate over each letter in the input text
        if letter in alphabet:  # Check if the letter is in the alphabet
            position = alphabet.index(letter)
            new_position = (position + shift_amount)  # Calculate the new position with wrapping
            new_letter = alphabet[new_position]  # Get the letter at the new position
            cipher_text += new_letter  # Append the new letter to the cipher text
        else:
            cipher_text += letter  # If the letter is not in the alphabet, add it unchanged (for spaces/punctuation)

    print(f"The encoded text is {cipher_text}")  # Output the encrypted message
## TODO-4: Decrypt
def decrypt(cipher_text , shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decode is {plain_text}")


# TODO-3: Call the encrypt function and pass in the user inputs
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)  # Call the encrypt function if the user wants to encode
elif  'decode':
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print ("Inval id Direction") # Handle invalid input


