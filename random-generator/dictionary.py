import itertools

# Open the English dictionary file
with open("dictionary.txt", "r", encoding="utf-8") as f:
    dictionary = [word.strip() for word in f.readlines()]

num_upper = int(input("Enter the number of uppercase letters: "))
num_lower = int(input("Enter the number of lowercase letters: "))
num_numbers = int(input("Enter the number of numbers: "))
use_special_chars = input("Do you want to include special characters? (y/n): ")

# Define the characters to use in the combinations
chars = "abcdefghijklmnopqrstuvwxyz"
chars_upper = chars.upper()
numbers = "0123456789"
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?\"'\\/"

if use_special_chars.lower() == "y":
    chars += special_chars

# Generate all possible combinations
combinations = itertools.product(
    chars_upper, repeat=num_upper)  # uppercase letters
combinations = itertools.product(
    combinations, chars, repeat=num_lower)  # lowercase letters
combinations = itertools.product(
    combinations, numbers, repeat=num_numbers)  # numbers
combinations = itertools.chain.from_iterable(combinations)
combinations = [''.join(comb) for comb in combinations]

# Filter the combinations that are in the dictionary
valid_combinations = set(combinations).intersection(dictionary)

# Save the valid combinations to a file
with open("generated.txt", "w", encoding="utf-8") as f:
    for comb in valid_combinations:
        f.write(comb + "\n")

# Create a new folder and move the generated file to it
import os
if not os.path.exists("Generated"):
    os.makedirs("Generated")
os.rename("generated.txt", os.path.join("Generated", "generated.txt"))
