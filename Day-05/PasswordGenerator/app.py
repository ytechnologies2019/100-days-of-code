import random  # Import the random module to use functions for generating random selections

# List of all lowercase and uppercase letters
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']

# List of digits from 1 to 9
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of special symbols
sym = ['!', '@', '#', '$', '%', '^', '*', '(', ')', '+', '-']

# Get user input for number of letters in the password
char_input = int(input("How many letters do you want to add?\n"))

# Get user input for number of numbers in the password
num_input = int(input("How many numbers do you want to add?\n"))

# Get user input for number of symbols in the password
symbol_input = int(input("How many symbols do you want to add?\n"))

# Initialize an empty password string
password = ""

# Add random letters to the password based on user input
for random_char in range(char_input):
    password += random.choice(char)  # Choose a random letter and append to password

# Add random numbers to the password based on user input
for random_num in range(num_input):
    password += random.choice(num)  # Choose a random number and append to password

# Add random symbols to the password based on user input
for random_sym in range(symbol_input):
    password += random.choice(sym)  # Choose a random symbol and append to password

# Convert the password string into a list to shuffle it
password_list = list(password)
random.shuffle(password_list)  # Shuffle the list to randomize the order of characters

# Reconstruct the password string from the shuffled list
password = ""  # Reset password string
for random_char in password_list:
    password += random_char  # Concatenate each character back into the password string

# Print the final randomized password
print(password)  # Display the generated password to the user
