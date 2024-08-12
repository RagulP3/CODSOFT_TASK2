import string
import random

def generate_password(length):
    if length < 4:
        return "Error! Password length should be at least 4."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        password = generate_password(length)
        print(f"Generated Password: {password}")

        another = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
