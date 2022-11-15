import string
import random

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
SYMBOLS = "~`! @#$%^&*()_-+={[}]|\:;<,>.?/'\""
NUMS = "0123456789"


def generate_password():
    letters = [letter for letter in LOWERCASE]
    letters += [letter for letter in UPPERCASE]
    symbols = [symbol for symbol in SYMBOLS]
    numbers = [number for number in NUMS]

    no_of_letters = random.randint(8, 10)
    no_of_symbols = random.randint(2, 4)
    no_of_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(no_of_letters)]
    password_list += [random.choice(numbers) for _ in range(no_of_numbers)]
    password_list += [random.choice(symbols) for _ in range(no_of_symbols)]
    random.shuffle(password_list)
    password = "".join(password_list)
    return password
