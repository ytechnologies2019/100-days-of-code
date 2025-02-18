PLACEHOLDER = "[name]"  # Match the correct placeholder

# Read all names and strip whitespace
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # Read as a list of names

#
# Read the template letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# # Loop through each name and generate a personalized letter
for name in names:
    stripped_name = name.strip()  # Remove extra spaces and newline
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    # Save the personalized letter
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
