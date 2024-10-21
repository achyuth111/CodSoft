import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password=".join(random.choice(characters)for_in range(length))"
    return password
if __name__ =='_ _main_ _':
    length=int(input("Enter the desired password length:"))
    password=generate_password(length)
    print("Generated password:",password)