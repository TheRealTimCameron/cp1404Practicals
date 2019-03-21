def main():

    password = get_password()
    for l in password:
        print_asterisks()
    print()


def print_asterisks():
    print("*", end='')


def get_password():
    password = input("Password: ")
    return password


main()