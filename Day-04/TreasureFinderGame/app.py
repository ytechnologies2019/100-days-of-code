line1 = ["⬜", "⬜", "⬜"]
line2 = ["⬜", "⬜", "⬜"]
line3 = ["⬜", "⬜", "⬜"]

print("Hiding your treasure X marks the spot.")
map = [line1, line2, line3]

position = input("Enter the position (e.g., A1): ")
letter = position[0].lower()
abc = ["a", "b", "c"]

# Find the index of the letter
letter_index = abc.index(letter)

# Get the row index from the position
number_index = int(position[1]) - 1  # X or second Digit B3 => 3

# Place the "X" in the correct position
map[number_index][letter_index] = "X"

# Print the map
diagram = f"{line1}\n{line2}\n{line3}"
print(diagram)