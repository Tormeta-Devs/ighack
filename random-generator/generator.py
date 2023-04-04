import itertools
import random
import os

# Ask if special characters should be included
special_characters = input("Do you want to include special characters? (y/n): ")

if special_characters.lower() == "y":
    # Define the characters to be combined, including special characters
    characters = "abcdefghijklmnopqrstuvwxyz!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
else:
    # Define the characters to be combined, without special characters
    characters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

# Ask for the number of uppercase and lowercase letters to include
num_uppercase = int(input("Enter the number of uppercase letters you want to include: "))
num_lowercase = int(input("Enter the number of lowercase letters you want to include: "))

# Ask for the number of numbers to include
num_numbers = int(input("Enter the number of numbers you want to include: "))

# Ask for the number of combinations to generate
num_combinations = int(input("Enter the number of combinations you want to generate: "))

# Calculate the total length of each combination
length = num_uppercase + num_lowercase + num_numbers

# Create a "Generated" directory in the parent directory
dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
generated_dir = os.path.join(dir_path, "Generated")
os.makedirs(generated_dir, exist_ok=True)

# Generate multiple combinations
for i in range(num_combinations):
    # Randomly choose the characters to use in each combination
    characters_comb = [random.choice(characters) for i in range(length-num_uppercase-num_lowercase-num_numbers)]
    uppercase_comb = [random.choice(uppercase_characters) for i in range(num_uppercase)]
    lowercase_comb = [random.choice(characters) for i in range(num_lowercase)]
    numbers_comb = [random.choice(numbers) for i in range(num_numbers)]

    # Combine all the characters
    characters_comb.extend(uppercase_comb)
    characters_comb.extend(lowercase_comb)
    characters_comb.extend(numbers_comb)

    # Shuffle the characters to generate unique combinations
    random.shuffle(characters_comb)

    # Convert the list of characters to a string
    combination = ''.join(characters_comb)

    # Write the combination to the "generated.txt" file in the "Generated" folder
    file_path = os.path.join(generated_dir, "generated.txt")
    with open(file_path, "a") as file:
        file.write(combination + "\n")

print(f"{num_combinations} combinations have been generated in the 'generated.txt' file in the 'Generated' folder.")