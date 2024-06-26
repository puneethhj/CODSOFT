import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected. Please select at least one character type.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("==================")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(e)

        another = input("Generate another password? (y/n): ").lower()
        if another != 'y':
            print("Exiting the password generator.")
            break

if __name__ == "__main__":
    main()
