def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_celcius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            get_fahrenheit()
        else:
            print("Invalid option")
        print(menu)
    print("Thank you")


def get_celcius(celsius):
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit


def get_fahrenheit():
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(celsius)


main()
