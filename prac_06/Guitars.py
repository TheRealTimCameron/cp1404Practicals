from prac_06.guitar import Guitar

def main():
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print("{} added.".format(new_guitar))
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars")
        for i, guitar in enumerate(guitars):
            vintage_guitar = ""
            if guitar.is_vintage():
                vintage_guitar = "(vintage)"
            print("Guitar {}: {:>2} ({}), worth $ {:1,.2f}{}".format(i + 1, guitar.name, guitar.year,
                                                                     guitar.cost, vintage_guitar))
    else:
        print("No guitars :( Quick, go and buy one!")

main()