import string
import secrets


def validate_options(options):
    options = options.replace(" ", "").upper()
    if len(options) > 3:
        print("[Error] You can't choose more than 3 options!")
        return -1

    for option in options:
        if option != 'A' and option != 'B' and option != 'C':
            print(f"[Error] {option} is an invalid option!")
            return -1

        if options.count(option) > 1:
            print(f"[Error] You can't repeat options!'")
            return -1

    return options


def validate_num(max_strings):
    if not max_strings.isnumeric():
        print("[ERROR] Only numeric positive values are valid!")
        return -1

    int_max_strings = int(float(max_strings))

    if int_max_strings == 0:
        print('Lol. Goodbye!')
        exit(0)

    return int_max_strings


print("""[::True Random::]
    [A]- Letters
    [B]- Numbers
    [C]- Punctuation""")

chosen_options = validate_options(input("Type your options: "))
while chosen_options == -1:
    chosen_options = validate_options(input("Type your options: "))

chosen_max = validate_num(input("\nNumber of random strings to generate: "))
while chosen_max == -1:
    chosen_max = validate_num(input("Number of random strings to generate: "))

chosen_len = validate_num(input("\nLength of random string: "))
while chosen_len == -1:
    chosen_len = validate_num(input("Length of random string: "))























