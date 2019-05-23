from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_input = input(">>> ")
    while menu_input != 'q':
        if menu_input == 'c':
            print('Taxis available')
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_input == 'd':
            current_taxi.start_fare()
            driving_distance = float(input("Drive how far? "))
            current_taxi.drive(driving_distance)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost
        else:
            print('invalid input')
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_input = input(">>> ")
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
