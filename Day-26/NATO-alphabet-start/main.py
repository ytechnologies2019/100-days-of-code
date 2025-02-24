import pandas  # Import the pandas library

# Read the NATO phonetic alphabet data from a CSV file
data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from the DataFrame where each letter maps to its phonetic code
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Ask the user for input and convert it to uppercase to match dictionary keys
user_input = input("Enter a word: ").upper()

# Convert each letter in the user input into its phonetic equivalent using dictionary lookup
output = [phonetic_dict[letter] for letter in user_input]  # List comprehension

# Print the final list of phonetic code words
print(output)
