import random
import string

letters = string.ascii_letters
chars = list(letters)
random.shuffle(chars)

def fibonacci_sequence(n):
    fib = [0, 1]
    while len(fib) < n + 2:  # Add 2 to ensure enough numbers are generated
        fib.append(fib[-1] + fib[-2])
    return fib[2:]  # Start the sequence from the third number

usr_inp = input("Please put a word below\n").replace(" ", "")
list_inp = list(usr_inp)
len_inp = len(usr_inp)  # encryption based on the length

fib_indices = fibonacci_sequence(len_inp)
print(fib_indices)
encrypted_message = [''] * max(fib_indices[-1] + 1, len_inp)  # Create a list of empty spaces

# Place letters into Fibonacci indices
for i, char in enumerate(list_inp):
    if i < len(fib_indices) and fib_indices[i] < len(encrypted_message):
        encrypted_message[fib_indices[i]] = char

# Fill non-Fibonacci indices with random characters
for i in range(len(encrypted_message)):
    if encrypted_message[i] == '':
        encrypted_message[i] = random.choice(chars)

# Convert list to string
encrypted_message_str = ''.join(encrypted_message)
print("Encrypted message:", encrypted_message_str)

def fibonacci_sequence_up_to(n):
    fib = [0, 1]
    while fib[-1] < n:  # Generate Fibonacci numbers up to the length of the encrypted message
        fib.append(fib[-1] + fib[-2])
    return fib[2:]  # Start from the third Fibonacci number

def decrypt_message(encrypted_message):
    # Generate Fibonacci indices based on the length of the encrypted message
    fib_indices = fibonacci_sequence_up_to(len(encrypted_message))
    
    # Extract the letters from Fibonacci indices
    decrypted_message = []
    for index in fib_indices:
        if index < len(encrypted_message):  # Ensure the index is within range
            decrypted_message.append(encrypted_message[index])
    
    return ''.join(decrypted_message)

# Example usage:
encrypted_message = input("Please insert an encrypted message here\n")

decrypted_message = decrypt_message(encrypted_message)
print("Decrypted message:", decrypted_message)
