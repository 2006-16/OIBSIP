import random
import string
print("   RANDOM PASSWORD GENERATOR")
try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Error: Password length must be greater than 0.")

    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

except ValueError:
    print("Error: Please enter a valid number.")
