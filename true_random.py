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


def filter_string(options):
    final_string = ""
    while options != "":
        secret_option = secrets.choice(options)
        if secret_option == "A":
            final_string += "".join(string.ascii_letters)
            options = options.replace(secret_option, "")

        if secret_option == "B":
            final_string += "".join(string.digits)
            options = options.replace(secret_option, "")

        if secret_option == "C":
            final_string += "".join(string.punctuation)
            options = options.replace(secret_option, "")

    return final_string


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

filtered_string = filter_string(chosen_options)
for current_string_index in range(0, chosen_max):
    true_random = ""
    for current_char_index in range(0, chosen_len):
        true_random += "".join(secrets.choice(filtered_string))
    print(true_random, "\n")
