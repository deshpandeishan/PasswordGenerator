from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, shuffle

lower_alpha = list(ascii_lowercase)
upper_alpha = list(ascii_uppercase)
all_digits = list(digits)
all_symbols = list(punctuation)

for _ in lower_alpha:
    lower_alpha[lower_alpha.index(_)] = choice(lower_alpha)

for _ in upper_alpha:
    upper_alpha[upper_alpha.index(_)] = choice(upper_alpha)

for _ in digits:
    all_digits[all_digits.index(_)] = choice(all_digits)

for _ in all_symbols:
    all_symbols[all_symbols.index(_)] = choice(all_symbols)


class Password:

    def __init__(self):
        self.password_list = []
        self.pass_str = ""

    def generate_password(self):
        for _ in range(l_alpha):
            self.password_list.append(lower_alpha[_])

        for _ in range(u_alpha):
            self.password_list.append(upper_alpha[_])

        for _ in range(digits):
            self.password_list.append(all_digits[_])

        for _ in range(symbols):
            self.password_list.append(all_symbols[_])

        shuffle(self.password_list)

        for _ in self.password_list:
            self.pass_str += str(_)

        return self.pass_str


print("Welcome to Random Password Generator")
print("Provide the number of digits you want in your password:")
l_alpha = int(input("Lowercase Alphabets: "))
u_alpha = int(input("Uppercase Alphabets: "))
digits = int(input("Numbers: "))
symbols = int(input("Symbols: "))

passkey = Password()
password = passkey.generate_password()
print(f"Your password is {password}.")
