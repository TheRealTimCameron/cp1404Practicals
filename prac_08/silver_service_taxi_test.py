from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Fancy Silver Taxi", 100, 2)
taxi.drive(18)
print(taxi)
print("Total trip cost: ${}".format(taxi.get_fare()))
